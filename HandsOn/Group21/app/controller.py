import pandas as pd
import streamlit as st

from rdflib import Graph, Namespace
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS, XSD

class AppController:
    def __init__(self, path):
        self.g = Graph()
        self.g.parse(path, format='turtle')

    st.cache
    def get_regions(self, settlement='District'):
        query = prepareQuery(f'''
            SELECT DISTINCT ?settlement_name
            WHERE {{
                ?settlement a <http://miciudadamiga.madrid/map/ontology#Madrid{settlement}>.
                ?settlement <http://miciudadamiga.madrid/map/ontology#hasName> ?settlement_name
            }}
        ''')
        return [r.settlement_name.value for r in self.g.query(query)]

    st.cache
    def get_total_centers_and_accessibility(self):
        ns = Namespace("http://miciudadamiga.madrid/map/ontology#")
        total = len(list(self.g.subjects(RDF.type, ns.DayCenter)))
    
        accessibility_query = prepareQuery('''
            SELECT (COUNT(DISTINCT ?center) AS ?center_count)
            WHERE {{
                ?center a <http://miciudadamiga.madrid/map/ontology#DayCenter>.
                ?center <http://miciudadamiga.madrid/map/ontology#hasAccesibility> true
            }}
        ''')
        accessibility = [r.center_count for r in self.g.query(accessibility_query)][0]
        return total, accessibility.value / total * 100

    st.cache
    def get_center_counts(self, settlement='District'):
        query = prepareQuery(f'''
            SELECT ?settlement_name (COUNT(DISTINCT ?center) AS ?center_count)
            WHERE {{
                ?center <http://miciudadamiga.madrid/map/ontology#belongsToMadrid{settlement}> ?settlement.
                ?center a <http://miciudadamiga.madrid/map/ontology#DayCenter>.
                ?settlement <http://miciudadamiga.madrid/map/ontology#hasName> ?settlement_name
            }}
            GROUP BY ?settlement
            ORDER BY DESC(?center_count)
        ''')

        index, column = [], []
        for r in self.g.query(query):
            index.append(r.settlement_name)
            column.append(r.center_count.value)

        return pd.DataFrame(index=index, data={'Cantidad de centros': column})

    def get_center_locations_by_region(self, settlement_name, settlement='District'):
        query = prepareQuery(f'''
            SELECT ?center_name ?longitude ?latitude ?address ?telephone ?openingHours ?accessByBusLines
            WHERE {{
                ?center a <http://miciudadamiga.madrid/map/ontology#DayCenter>.
                ?center <http://miciudadamiga.madrid/map/ontology#belongsToMadrid{settlement}> ?settlement.
                ?center <http://schema.org/name> ?center_name.
                ?center <http://schema.org/address> ?address.
                ?center <http://schema.org/telephone> ?telephone.
                ?center <http://schema.org/openingHours> ?openingHours.
                ?center <http://miciudadamiga.madrid/map/ontology#accessByBusLines> ?accessByBusLines.
                ?center <http://schema.org/latitude> ?latitude.
                ?center <http://schema.org/longitude> ?longitude.
                ?settlement <http://miciudadamiga.madrid/map/ontology#hasName> "{settlement_name}"
            }}
        ''')
        data = {'Name': [], 'lat': [], 'lon': [], 'Dirección': [],
                'Teléfono': [], 'Horario': [], 'Líneas de Bus': []}
        for r in self.g.query(query):
            data['lat'].append(float(r.latitude))
            data['lon'].append(float(r.longitude))
            data['Name'].append(r.center_name.value)
            data['Dirección'].append(r.address.value)
            data['Teléfono'].append(r.telephone.value)
            data['Horario'].append(r.openingHours.value)
            data['Líneas de Bus'].append(r.accessByBusLines.value)

        return pd.DataFrame(data=data)

    def get_subway_stops(self):
        query = prepareQuery('''
            SELECT DISTINCT ?subway_name
            WHERE {{
                ?subwayStop a <http://miciudadamiga.madrid/map/ontology#SubwayStop>.
                ?subwayStop <http://miciudadamiga.madrid/map/ontology#hasName> ?subway_name
            }}
        ''')
        return [r.subway_name.value.replace('_', ' ') for r in self.g.query(query)]

    def get_centers_by_subway_stop(self, subway_name):
        query = prepareQuery(f'''
            SELECT ?center_name ?longitude ?latitude ?address ?telephone ?openingHours ?accessByBusLines
            WHERE {{
                ?center a <http://miciudadamiga.madrid/map/ontology#DayCenter>.
                ?center <http://schema.org/name> ?center_name.
                ?center <http://schema.org/latitude> ?latitude.
                ?center <http://schema.org/longitude> ?longitude.
                ?center <http://schema.org/address> ?address.
                ?center <http://schema.org/telephone> ?telephone.
                ?center <http://schema.org/openingHours> ?openingHours.
                ?center <http://miciudadamiga.madrid/map/ontology#accessByBusLines> ?accessByBusLines.
                ?center <http://miciudadamiga.madrid/map/ontology#hasMetroAccess> ?subwayStop.
                ?subwayStop <http://miciudadamiga.madrid/map/ontology#hasName> "{subway_name}"
            }}
        ''')

        data = {'Name': [], 'lat': [], 'lon': [], 'Dirección': [],
                'Teléfono': [], 'Horario': [], 'Líneas de Bus': []}
        for r in self.g.query(query):
            data['lat'].append(float(r.latitude))
            data['lon'].append(float(r.longitude))
            data['Name'].append(r.center_name.value)
            data['Dirección'].append(r.address.value)
            data['Teléfono'].append(r.telephone.value)
            data['Horario'].append(r.openingHours.value)
            data['Líneas de Bus'].append(r.accessByBusLines.value)

        return pd.DataFrame(data=data)

    def get_center_by_subway_stop_number(self, number):
        query = prepareQuery(f'''
            SELECT ?center_name ?longitude ?latitude
            WHERE {{
                ?center a <http://miciudadamiga.madrid/map/ontology#DayCenter>.
                ?center <http://schema.org/name> ?center_name.
                ?center <http://schema.org/latitude> ?latitude.
                ?center <http://schema.org/longitude> ?longitude.
                ?center <http://miciudadamiga.madrid/map/ontology#hasMetroAccess> ?subwayStop
            }}
            GROUP BY ?center
            HAVING (COUNT(DISTINCT ?subwayStop) >= {number})
        ''')

        data = {'Name': [], 'lat': [], 'lon': []}
        for r in self.g.query(query):
            data['lat'].append(float(r.latitude))
            data['lon'].append(float(r.longitude))
            data['Name'].append(r.center_name.value)

        return pd.DataFrame(data=data)
