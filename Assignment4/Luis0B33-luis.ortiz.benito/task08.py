
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal, URIRef
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")

"""Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas."""

ns=Namespace("http://data.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

query1 = prepareQuery("""
  SELECT ?person ?given ?family ?mail WHERE{    
      ?person a ns:Person.
      OPTIONAL { ?person vcard:Given ?given}
      OPTIONAL { ?person vcard:Family ?family}
      OPTIONAL { ?person vcard:EMAIL ?mail}
  }
  """, initNs = {
      "ns":ns,
      "rdfs":RDFS,
      "vcard":VCARD
  }
)

# query2 = prepareQuery("""
#   SELECT ?person ?given ?family ?mail WHERE{    
#       ?person a ns:Person.
#       OPTIONAL { ?person vcard:Given ?given}
#       OPTIONAL { ?person vcard:Family ?family}
#       OPTIONAL { ?person vcard:EMAIL ?mail}
#   }
#   """, initNs = {
#       "ns":ns,
#       "rdfs":RDFS,
#       "vcard":VCARD
#   }
# )
# for r in g2.query(query2):
#   print(r.person, r.given, r.family, r.mail)

from logging import exception

def fixInstance(graphToFix, instance, missingFields, supportGraph):
  if instance["person"] is None: exception("Fatal error, person identifier cant be None")
  print(f"---Missing field on- instance {instance['person']} fixing it...--")
  for key in instance:
    if instance[key] is None:
      print(f"-Adding missing {key}...")
      for (person,property,value) in supportGraph.triples((instance["person"],missingFields[key],None)): 
        graphToFix.add((instance["person"],missingFields[key],value))
  print(f"---Instance fixed succesfully!...--")


Fields = {
    "given": VCARD.Given, 
    "family": VCARD.Family,
    "mail": VCARD.EMAIL
  }

for r in g1.query(query1):
  instance = {
    "person": r.person,
    "given": r.given, 
    "family": r.family,
    "mail": r.mail
  }
  if None in r: fixInstance(g1, instance, Fields, g2)

for r in g1.query(query1):
  instance = {
    "person": r.person,
    "given": r.given, 
    "family": r.family,
    "mail": r.mail
  }
  print(instance)
  print(None in r)