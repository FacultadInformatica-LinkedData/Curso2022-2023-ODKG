# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1JH0SxhmFkNxfZ_9XQwQlsOOdcETMjMWG

**Task 07: Querying RDF(s)**
"""

#!pip install rdflib 
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
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
# Visualize the results
#RDFLib
print("RDFLib")
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
    print(s)

#SPARQL
print("\nSPARQL")
q1 = prepareQuery('''
  SELECT ?subcl WHERE { 
    ?subcl rdfs:subClassOf ns:Person . 
  }
  ''',
  initNs={'rdfs':RDFS, 'ns':ns}
)
for r in g.query(q1):
  print(r.subcl)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
# Visualize the results
#RDFLib
print("RDFLib")
for s,p,o in g.triples((None,RDF.type,ns.Person)) :
  print(s)

for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)) :
  for s2,p1,o1 in g.triples((None,RDF.type,s)) :
    print(s2)

#SPARQL
print("\nSPARQL")
q2 = prepareQuery('''
  SELECT  ?i  WHERE 
  {
    ?sub rdfs:subClassOf* ns:Person .
    ?i a ?sub
  }  
  ''',initNs={'rdfs':RDFS, 'ns':ns}
)

for r in g.query(q2):
  print(r.i)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results
#RDLib
print("RDLib")
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for s2, p2, o2 in g.triples((s, None, None)):
        print(s2, p2, o2)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s2, p2, o2 in g.triples((None, RDF.type, s)):
    for s3, p3, o3 in g.triples((s2, None, None)):
       print(s3, p3, o3)

#SPARQL
print("\nSPARQL")
q3 = prepareQuery('''
  SELECT ?i ?prop ?value WHERE {
    ?sub rdfs:subClassOf* ns:Person .
    ?i a ?sub .
    ?i ?prop ?value
  }
  ''', initNs={"rdfs": RDFS, "ns": ns}
) 

for r in g.query(q3):
  print(r.i, r.prop, r.value)