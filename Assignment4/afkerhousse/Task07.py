#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[8]:


# TO DO
ns = Namespace("http://somewhere#")
from rdflib.plugins.sparql import prepareQuery

#RDFLib
print("Results with RDFLib")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

#SPARQL
print("Results with SPARQL")
q1 = q1 = prepareQuery('''
  SELECT ?Sub WHERE { 
    ?Sub rdfs:subClassOf ns:Person. 
    }
  ''',
  initNs = { "ns": ns,
            "rdfs": RDFS}
)
for r in g.query(q1): 
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[9]:


# TO DO

#RDFLib
print("Results with RDFLib")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1,p1,o1 in g.triples((None, RDF.type, s)):
        print(s1)

#SPARQL
print("Results with SPARQL")
q2 = prepareQuery('''
  SELECT ?Ind WHERE { 
    ?subclass rdfs:subClassOf* ns:Person.
    ?Ind rdf:type ?subclass. 
    }
  ''',
  initNs = {"ns":ns,
            "rdf":RDF,
            "rdfs":RDFS
            }
)
for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[21]:


# TO DO

#RDFLib
print("Results with RDFLib")
for s1,p1,o1 in g.triples((None, RDF.type, ns.Person)):
  print(f"Individual {s1}")
  for s2,p2,o2 in g.triples((s1,None,None)):
    print(f"Property: {p2}, Value: {o2}")
for s1,p1,o1 in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s2,p2,o2 in g.triples((None, RDF.type, s1)):
    print(f"Individual {s2}")
    for s3,p3,o3 in g.triples((s2,None,None)):
      print(s3,p3,o3)

#SPARQL
print("Results with SPARQL")
q3 = prepareQuery('''
  SELECT ?Ind ?prop ?class WHERE { 
    ?subclass rdfs:subClassOf* ns:Person.
    ?Ind a ?subclass.
    ?Ind ?prop ?class
    }
  ''',
  initNs = {"ns":ns,
            "rdf":RDF,
            "rdfs":RDFS,
            }
)
for r in g.query(q3):
  print(r)

