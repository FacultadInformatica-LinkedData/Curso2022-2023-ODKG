# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11FsWUiErRfFTlmidC1XJQA3gV4giLFMD

**Task 07: Querying RDF(s)**
"""

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

# TO DO
# Visualize the results
from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

###

query = prepareQuery("""
  SELECT ?subject
  WHERE {
    ?subject rdfs:subClassOf+  <http://somewhere#Person>.
  }
""")

for result in g.query(query):
  print(result)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for ss, pp, oo in g.triples((None, RDF.type, s)):
      print(ss)

for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)

query = prepareQuery("""
  SELECT ?subject
  WHERE {
    ?subject rdf:type/rdfs:subClassOf* <http://somewhere#Person>.
  }
"""
)

for result in g.query(query):
  print(result)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results

for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for ss, pp, oo in g.triples((s, None, None)):
    print(ss, pp)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for ss, pp, oo in g.triples((None, RDF.type, s)):
    for sss, ppp, ooo in g.triples((ss, None, None)):
      print(sss, ppp)

query = prepareQuery("""
  SELECT ?subject ?property
  WHERE {
    ?subject rdf:type/rdfs:subClassOf* <http://somewhere#Person>.
    ?subject ?property ?value.
  }
""")

for result in g.query(query):
  print(result)