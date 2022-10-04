# -*- coding: utf-8 -*-
"""Task07.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-7OK1zr8jJ9TAtSdR35TNgXUCB1sXszk

**Task 07: Querying RDF(s)**
"""

!pip install rdflib 
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
from rdflib import FOAF

q1 = prepareQuery('''
  SELECT ?Class WHERE {
    ?Class rdfs:subClassOf ?Person. 
  }
  ''',
  initNs = { "rdfs": RDFS}
)
# Visualize the results
for r in g.query(q1):
  print(r)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

# TO DO
q2 = prepareQuery('''
  SELECT ?individ WHERE {
    ?individ rdf:type ?sclass.
    ?sclass rdf:type/rdfs:subClassOf* ?Person.
  }
  ''',
  initNs = { "rdfs": RDFS}
)
# Visualize the results
for r in g.query(q2):
  print(r)

#for s, p, o in g:
  #print(s, p, o)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

# TO DO
# Visualize the results
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

q2 = prepareQuery('''
  SELECT ?FN ?Given ?Family ?Email ?sclass WHERE {
    ?individ rdf:type ?sclass.
    ?sclass rdf:type/rdfs:subClassOf* ?Person.
    ?individ vcard:FN ?FN.
    ?individ vcard:Given ?Given.
    ?individ vcard:Family ?Family.
    ?individ vcard:Email ?Email.

  }
  ''',
  initNs = { "rdfs": RDFS, "vcard": VCARD}
)
# Visualize the results
for r,a,b,c,d in g.query(q2):
  print(r,a,b,c,d)