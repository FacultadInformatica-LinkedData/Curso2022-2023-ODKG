# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/github/DCY1117/Curso2022-2023-ODKG/blob/master/Assignment4/course_materials/notebooks/Task07.ipynb

**Task 07: Querying RDF(s)**
"""

# pip install rdflib, Terminal
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery

# TO DO
print("RDFLib##########")

ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

print("SPARQL##########")

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person.
  } 
  ''',
  initNs = { "ns": ns}
)

# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
print("RDFLib##########")

for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, p1, o1 in g.triples((None, RDF.type, s)):
    print(s1)
  
print("SPARQL##########")

# elt*, A path of zero or more occurrences of elt

q1 = prepareQuery('''
  SELECT ?Subject ?class WHERE { 
    ?class rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?class
  } 
  ''',
  initNs = { "ns": ns}
)

# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
print("RDFLib##########")

for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s, None, None)):
    print(s1, p1, o)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s1, p1, o1 in g.triples((None, RDF.type, s)):
    for s2, p2, o2 in g.triples((s1, None, None)):
      print(s2, p2, s)

print("SPARQL##########")

q1 = prepareQuery('''
  SELECT ?Subject ?prop ?class WHERE { 
    ?class rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?class.
    ?Subject ?prop ?o. 
  } 
  ''',
  initNs = { "ns": ns}
)

# Visualize the results
for r in g.query(q1):
  print(r)