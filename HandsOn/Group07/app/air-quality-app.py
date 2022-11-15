import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import plotly.express as px
import folium
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS, SKOS
from rdflib.plugins.sparql import prepareQuery



st.set_page_config(page_title='Air Quality')
st.header('Results for 2021')
st.subheader('Choose your filters')

g = Graph()
g.parse("./src/airquality-data-with-links.nt")

g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace(
    "http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)

g.namespace_manager.bind('vocab', Namespace(
    "http://smartcity.airquality.es/airquality/"), override=True)
g.namespace_manager.bind('saref', Namespace(
    "https://saref.etsi.org/core/v3.1.1/"), override=True)

VOCAB = Namespace("http://smartcity.airquality.es/airquality/")
SAREF = Namespace("https://saref.etsi.org/core/v3.1.1/")
owl = Namespace("http://www.w3.org/2002/07/owl#")
RDFS = RDFS
RDF = RDF

# 1. Select stations
q1 = prepareQuery('''
SELECT ?station ?name
  WHERE {
    ?station rdf:type vocab:Station .
    ?station vocab:hasStationName ?name
  }

''',
                  initNs={
                      "rdfs": RDFS,
                      "rdf": RDF,
                      "vocab": VOCAB,
                      "saref": SAREF
                  })

stations = []

for r in g.query(q1, initBindings={'?Class': VOCAB.Station}):
    stations.append(r.name)

# Dataframe for stations
stations_df = pd.DataFrame(stations, columns=['Station'])

# Display stations on the web
stations_selection = st.multiselect('Stations',
                                    stations_df,
                                    default=stations[16])

# 2. Select coordinates for choosen stations
q2 = prepareQuery('''
  SELECT ?station ?name ?Loc ?lat ?lon
  WHERE {
    ?station rdf:type vocab:Station .
    ?station vocab:hasStationName ?name .
    ?station vocab:isLocatedIn ?Loc .
    ?station vocab:latitude ?lat .
    ?station vocab:longitude ?lon
  }

''',
                  initNs={
                      "rdfs": RDFS,
                      "rdf": RDF,
                      "vocab": VOCAB,
                      "saref": SAREF
                  })

# Dataframe for coordinates
df_coordinates = pd.DataFrame(
    {'Latitude': [], 'Longitude': [], 'Station_Name': []})

print("Recording coordinates")
for a in stations_selection:
    print("Station", a)
    for r in g.query(q2, initBindings={'name': Literal(a)}):
        temporary = pd.DataFrame(
            {'Latitude': [r.lat], 'Longitude': [r.lon], 'Station_Name': [r.name]})
        df_coordinates = df_coordinates.append(temporary, ignore_index=True)


print("Coordinates DF\n", df_coordinates)

# Display the map
my_map = folium.Map(
    location=[40.4165, -3.70256],
    zoom_start=9
)

# Display the stations selected
for _, station in df_coordinates.iterrows():
    folium.Marker(
        location=[station['Latitude'], station['Longitude']],
        popup='<h4>'+station['Station_Name']+'</h4>'
        + '<br>Coordinates ['+station['Latitude'] +
        station['Longitude']+']</br>',
        tooltip='<h4>'+station['Station_Name']+'</h4>',
        icon=folium.Icon(color='blue', prefix='fa',
                         icon='circle')
    ).add_to(my_map)

folium_static(my_map)



station_selected_for_magnitude = st.selectbox('Stations', stations)

print("Stations Selected for Magnitude:", station_selected_for_magnitude)


#Display the value of the magnitude (sulfur dioxide) by station
q3 = prepareQuery('''
SELECT DISTINCT ?name ?magName ?value ?date 
  WHERE {
      ?station rdf:type vocab:Station .
      ?station vocab:hasStationName ?name .
      
      ?magnitude rdf:type vocab:Magnitude .
      ?magnitude vocab:hasMagnitudeName ?magName .
      ?magnitude saref:hasValue ?value .
      ?magnitude saref:hasTimestamp ?date

      FILTER(?magName = "sulfur dioxide")
      FILTER(?value > 6 && ?value < 12)
      FILTER(MONTH(?date) > 0 && MONTH(?date) <6)    
     
    
  }
  LIMIT 20
  

''',
                  initNs={
                      "rdfs": RDFS,
                      "rdf": RDF,
                      "vocab": VOCAB,
                      "saref": SAREF
                  })

df_magnitudes = pd.DataFrame({'Date': [], 'Values': []})
df_test = pd.DataFrame(
    {"Station": [], 'Magnitude': [], 'Values': [], 'Date': []})

for r in g.query(q3, initBindings={'name': Literal(station_selected_for_magnitude)}):
    df2 = pd.DataFrame({'Date': [r.date], 'Values': [r.value]})
    df_magnitudes = df_magnitudes.append(df2, ignore_index=True)
    # Only for test
    df3 = pd.DataFrame({'Station': [r.name], 'Magnitude': [r.magName], 'Values': [r.value], 'Date': [
        r.date]})
    df_test = df_test.append(df3, ignore_index=True)
    # -------------

print("Magnitude Selected\n", df_magnitudes)

print("Test Selected\n", df_test)

test_df_other = pd.DataFrame({'Date': ["2021-01-01", "2021-02-01", "2021-03-01",
                             "2021-04-01", "2021-05-01"], 'Values': [7, 4, 12, 9, 10]})

bar_chart = px.bar(df_magnitudes,
                   x='Date',
                   y='Values',
                   title="Magnitude Bar - Sulfur Dioxide",
                   template='plotly_white')

st.plotly_chart(bar_chart)
