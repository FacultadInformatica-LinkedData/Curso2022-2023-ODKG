# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1n7uOg7lh2EdAhW2pfOXJzERs_Du3_ZVJ

**saavedrAndrei - Andrei Saavedra**

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

from rdflib.plugins.sparql import prepareQuery

"""**SPARQL**"""

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://somewhere#http://www.w3.org/2001/vcard-rdf/3.0/")
RDFS = RDFS

q1 = prepareQuery('''
SELECT ?s ?p ?o 
WHERE {
  ?s rdfs:subClassOf ns:Person
}
''',
initNs = {
    "ns": NS,
    "vcard-rdf": VCARD,
    "rdfs" : RDFS
})

for r in g.query(q1):
  print(r.s)

"""**RDFLib**"""

ns = Namespace("http://somewhere#")

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

**SPARQL**
"""

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://somewhere#http://www.w3.org/2001/vcard-rdf/3.0/")
RDFS = RDFS
RDF = RDF

q2 = prepareQuery('''
SELECT ?x ?prop ?o
  WHERE {
    ?class rdfs:subClassOf* ns:Person .
    ?x a ?class .
  }

''',
initNs = {
    "ns": NS,
    "vcard-rdf": VCARD,
    "rdfs" : RDFS,
    "rdf": RDF
})

for r in g.query(q2):
  print(r.x)

"""**RDFLib**"""

ns = Namespace("http://somewhere#")

for s1,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s1)

for s2,p2,o2 in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s3, p3, o3 in g.triples((None, RDF.type, s2)):
    print(s3)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

**SPARQL**
"""

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://somewhere#http://www.w3.org/2001/vcard-rdf/3.0/")
RDFS = RDFS
RDF = RDF

q3 = prepareQuery('''
  SELECT ?x ?prop ?o
  WHERE {
    ?class rdfs:subClassOf* ns:Person .
    ?x a ?class .
    ?x ?prop ?o .
  }
''',
initNs = {
    "ns": NS,
    "vcard-rdf": VCARD,
    "rdfs" : RDFS,
    "rdf": RDF
})

for r in g.query(q3):
  print(r.x, r.prop, r.o)

"""**RDFLib**"""

ns = Namespace("http://somewhere#")

for s0, p0, o0 in g.triples((None, RDF.type, ns.Person)):
  for s1, p1, o1 in g.triples((s0, None, None)):
    print(s0, p1, o1)

for s2, p2, o2, in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s3, p3, o3 in g.triples((None, RDF.type, s2)):
    for s4, p4, o4 in g.triples((s3, None, None)):
      print(s3, p4, o4)

