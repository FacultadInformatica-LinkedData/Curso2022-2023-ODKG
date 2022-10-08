github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

ns = Namespace("http://somewhere#")

for s, p, o in g:
    print(s, p, o)

""" Task 7.1 """
print("Task 7.1 SPARQL")
print("------------------------------")
sparql_query = """ select distinct ?subClass where
{
    ?subClass <http://www.w3.org/2000/01/rdf-schema#subClassOf> <http://somewhere#Person>.
}
"""
result = g.query(sparql_query)
for row in result:
    print(f"{row.subClass}")

print("------------------------------\n")

print("Task 7.1 RDFlib")
print("------------------------------")

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

print("------------------------------\n")


""" Task 7.2 """
print("Task 7.2")
print("------------------------------")
sparql_query = """ select distinct ?instance where
{
    ?class <http://www.w3.org/2000/01/rdf-schema#subClassOf>* <http://somewhere#Person>.
    ?instance <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?class.
}
"""
result = g.query(sparql_query)
for row in result:
    print(f"{row.instance}")

print("------------------------------\n")

print("Task 7.2 RDFlib")
print("------------------------------")

def get_instance_nested_classes(class_):
    for s, p, o in g.triples((None, RDF.type, class_)):
        print(s)
    for s, p, o in g.triples((None, RDFS.subClassOf, class_)):
        get_instance_nested_classes(s)

get_instance_nested_classes(ns.Person)
       

print("------------------------------\n")

""" Task 7.3 """
print("Task 7.3")
print("------------------------------")
sparql_query = """ select distinct ?instance ?property ?value ?instanceClass where
{
    ?class <http://www.w3.org/2000/01/rdf-schema#subClassOf>* <http://somewhere#Person>.
    ?instance <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ?class;
    ?property ?value.
}
"""
result = g.query(sparql_query)
for row in result:
    print(f"Individual: {row.instance}, property: {row.property}, value: {row.value}")

print("------------------------------\n")

print("Task 7.3 RDFlib")
print("------------------------------")

def get_properties_nested_classes(class_):
    for s, p, o in g.triples((None, RDF.type, class_)):
        for s, p, o in g.triples((s, None, None)):
            print(f"Individual: {s}, property: {p}, value: {o}")
    for s, p, o in g.triples((None, RDFS.subClassOf, class_)):
        get_properties_nested_classes(s)

get_properties_nested_classes(ns.Person)

print("------------------------------\n")
