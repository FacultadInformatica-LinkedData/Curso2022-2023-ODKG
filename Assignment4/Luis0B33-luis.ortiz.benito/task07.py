"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# Done
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")

query1 = prepareQuery("""
  SELECT ?subclass WHERE{
    ?subclass RDFS:subClassOf ns:Person.
  }
  """, initNs = {
      "ns":ns,
      "RDFS":RDFS
  }

)
# Visualize the results
for r in g.query(query1):
  print(r.subclass)
#rdflib 
#RDFLIB
for subclass, property, value in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(f"{subclass}")
"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""
#SPARQL

#DONE
query2 = prepareQuery("""
  SELECT ?person WHERE{
    {
      ?person a ns:Person.
    } UNION {
      ?subclass RDFS:subClassOf ns:Person.
      ?person a ?subclass.
    }
  }
  """, initNs = {
      "ns":ns,
      "RDFS":RDFS
  }
)

# Visualize the results
for r in g.query(query2):
  print(r.person)
#RDFLIB
for individual, property, value in g.triples((None, RDF.type, ns.Person)):
  print(f"{individual}")
for subclass, prop, val in g.triples((None, RDFS.subClassOf, ns.Person)):
  for individual, property, value in g.triples((None, RDF.type, subclass)):
    print(f"{individual}")


"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""
#SPARQL
#DONE
query3 = prepareQuery("""
  SELECT ?subclass ?person ?property  WHERE{
    {
      ?person a ns:Person.
    } UNION {
      ?subclass RDFS:subClassOf ns:Person.
    }
    ?person a ?subclass.
    ?person ?property ?value.
  }
  """, initNs = {
      "ns":ns,
      "RDFS":RDFS
  }
)

# Visualize the results
for r in g.query(query3):
  print(r.subclass, r.person, r.property)

#RDFLIB
for individual, prop, val in g.triples((None, RDF.type, ns.Person)):
  for individual, property, value in g.triples((individual, None, None)):
    print(f"{individual} {property} {value}")

for subclass, prop, val in g.triples((None, RDFS.subClassOf, ns.Person)):
  for ind, pro, va in g.triples((None, RDF.type, subclass)):
    for individual, property, value in g.triples((individual, None, None)):
      print(f"{individual} {property} {value}")

