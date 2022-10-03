
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

for s, p, o in g:
  print (s, p, o)

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO

NS = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
  SELECT ?Sub WHERE { 
    ?Sub RDFS:subClassOf* ns:Person.
    FILTER(?Sub != ns:Person)
  } 
  ''',
  initNs = { "ns": NS, "RDFS" : RDFS}
)

# Visualize the results

for r in g.query(q1):
  print(r.Sub)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery('''
  SELECT ?Persons WHERE { 
    {
      ?Sub RDFS:subClassOf* ns:Person.
      ?Persons RDF:type ?Sub.
    }
  }
  ''',
  initNs = { "ns": NS, "RDF" : RDF, "RDFS" : RDFS}
)

for r in g.query(q2):
  print(r.Persons)
# Visualize the results

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
q3 = prepareQuery('''
  SELECT ?Persons ?Properties WHERE { 
    {
      ?Sub RDFS:subClassOf* ns:Person.
      ?Persons RDF:type ?Sub.
      ?Persons ?a ?Properties
    }
  }
  ''',
  initNs = { "ns": NS, "RDF" : RDF, "RDFS" : RDFS}
)

for r in g.query(q3):
  print(r.Persons, r.Properties)
# Visualize the results