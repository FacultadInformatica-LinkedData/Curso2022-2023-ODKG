
'''An example of what we can do with the Linked data'''

from json import load
from pyexpat.errors import codes
import streamlit as st
import pandas as pd
import numpy as np
from SPARQLWrapper import SPARQLWrapper,JSON

from rdflib import Graph, Namespace, Literal, XSD
from rdflib.plugins.sparql import prepareQuery

# SETTING PAGE CONFIG TO WIDE MODE, PAGE TITLE AND ADDING A FAVICON
st.set_page_config(layout="wide", page_title='Bus Stop Search', page_icon=":bus:")

# LOAD STOP CODE ONCE
@st.experimental_singleton
def load_stop_codes():
    g = Graph()
    g.parse("busstop-with-links_updated.ttl",format="ttl")
    ns = Namespace("http://busstopalcobendas.odkg.es/group15/ontology/gr15#")
    q = prepareQuery('''
        SELECT ?code
        WHERE { 
            ?s  ns:stop_code ?code.
        }
        ''',
        initNs = { "ns": ns}
    )
    codes = []
    for r in g.query(q):
        codes.append(str(r.code))
    codes.append('')

    return codes

stop_codes = load_stop_codes()

# # LOAD STREET NAME ONCE
@st.experimental_singleton
def load_street_names():
    g = Graph()
    g.parse("busstop-with-links_updated.ttl",format="ttl")
    base = Namespace("http://busstopalcobendas.odkg.es/group15/ontology/gr15#")
    q = prepareQuery('''
        SELECT DISTINCT ?address_name
        WHERE { 
            ?Subject base:hasAddress ?address.
            ?address base:street_name ?address_name.
        }
        ''',
        initNs = { "base": base}
    )
    street_names = []
    for r in g.query(q):
        street_names.append(str(r.address_name))
    street_names.append('')
    return street_names

street_names = load_street_names()

# MAP OF ALL BUS STOP
def todo(): # El mapa de todas las paradas
    g = Graph()
    g.parse("busstop-with-links_updated.ttl",format="ttl")
    wikidata = SPARQLWrapper("https://query.wikidata.org/sparql")
    ns = Namespace("http://busstopalcobendas.odkg.es/group15/ontology/gr15#")
    q = prepareQuery('''
        SELECT *
        WHERE { 
            ?s  ns:stop_lat ?o.
            ?s  ns:stop_lon ?o2
        }
        ''',
        initNs = { "ns": ns}
    )
    lat = []
    lon = []
    for r in g.query(q):
        lat.append(float(r.o))
        lon.append(float(r.o2))
    df = pd.DataFrame(np.array([lat,lon]).transpose(),columns=['lat','lon'])
    st.map(df)


# SEARCH BY STOP CODE    
def find_stop_by_code(code): #La info de la parada 12723
    g = Graph()
    g.parse("busstop-with-links_updated.ttl", format="ttl")
    wikidata = SPARQLWrapper("https://query.wikidata.org/sparql")
    base = Namespace("http://busstopalcobendas.odkg.es/group15/ontology/gr15#")
    owl = Namespace("http://www.w3.org/2002/07/owl#")
    query = '''
    SELECT ?name ?address_name ?address_num ?lon ?lat ?zone ?link WHERE {{
        ?Subject base:stop_code \"{0}\".
        ?Subject base:stop_name ?name.
        ?Subject base:hasAddress ?address.
        ?address base:street_name ?address_name.
        ?address base:street_number ?address_num.
        ?Subject base:stop_lon ?lon.
        ?Subject base:stop_lat ?lat.
        ?Subject base:zone_id ?zone.
        OPTIONAL {{?address owl:sameAs ?link.}}
    }} 
    '''
    q = prepareQuery(query.format(code),initNs={"base": base, "owl": owl})
    l = []
    for r in g.query(q):
        l.append(r)
    df = pd.DataFrame(l, columns =['stop_name', 'street_name', 'street_number', 'stop_longitude', 'stop_latitude', 'stop_zone', 'link to the street name'])

    col1, col2 = st.columns((1,1))
    with col1:
        if df.empty:
            st.text('Nope')
        else :
            st.text(df.T.to_string(header=False))
            if not df['link to the street name'].loc[df.index[0]] == None:
                query = '''
                SELECT ?obj ?objLabel WHERE {{
                    wd:{0} wdt:P2789 ?obj.
                    SERVICE wikibase:label {{ bd:serviceParam wikibase:language "en" }}
                }} 
                '''

                wikidata.setQuery(query.format(df['link to the street name'].loc[df.index[0]].split('/')[-1]))

                wikidata.setReturnFormat(JSON)
                results = wikidata.query().convert()

                results_df = pd.io.json.json_normalize(results['results']['bindings'])
                if results_df.empty:
                    with col2:
                        st.text('Nope')
                else:
                    with col2:
                        st.text('Connects with:\n' + results_df['objLabel.value'].to_string(index=False))
            else:
                with col2:
                    st.text('Nope')
    



# SEARCH BUS STOP IN CERTAIN STREET
def all_bus_stops_on_a_street(street):  # All bus stops on the street "Avenida de Burgos"
    g1 = Graph()
    g1.parse("busstop-with-links_updated.ttl", format="ttl")
    wikidata = SPARQLWrapper("https://query.wikidata.org/sparql")
    base = Namespace("http://busstopalcobendas.odkg.es/group15/ontology/gr15#")
    owl = Namespace("http://www.w3.org/2002/07/owl#")
    query = '''
    SELECT ?code ?name ?lon ?lat ?zone ?link WHERE {{
        ?Subject base:stop_code ?code.
        ?Subject base:stop_name ?name.
        ?Subject base:hasAddress ?address.
        ?address base:street_name ?address_name.
        ?Subject base:stop_lon ?lon.
        ?Subject base:stop_lat ?lat.
        ?Subject base:zone_id ?zone.
        OPTIONAL {{?address owl:sameAs ?link.}}
        FILTER regex(str(?address_name), '{0}').
    }} 
    '''
    q1 = prepareQuery(query.format(street),initNs={"base": base, "owl": owl})
    l = []
    for r in g1.query(q1):
        l.append(r)
    df = pd.DataFrame(l, columns =['stop_code', 'stop_name', 'stop_longitude', 'stop_latitude', 'stop_zone', 'link to the street name'])

    if df.empty:
        st.text('Nope')
    else:
        st.text(df.to_string(index=False))


# Streamlit layout
st.title('Bus Stop Search (Alcobendas) 🚏')

option = st.selectbox(
    'Search by',
    ('All', 'Stop code', 'Street name'))

if option == 'All':
    if st.button('Search'):
        todo()

if option == 'Stop code': # '12723'
    code = st.selectbox(
    'Stop code', 
    stop_codes,len(stop_codes)-1)

    if st.button('Search'):
        find_stop_by_code(code)

if option == 'Street name': # 'Avenida de Burgos'

    street = st.selectbox(
    'Street name',
    street_names, len(street_names)-1)

    if st.button('Search'):
        all_bus_stops_on_a_street(street)
        