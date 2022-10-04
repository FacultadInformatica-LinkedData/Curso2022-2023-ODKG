#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[32]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[33]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[39]:


# TO DO

NS = Namespace("http://somewhere#")

# rdflib
print("Using sparql: ")
for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  print(s)

# sparql
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
  SELECT ?sc WHERE { 
    ?sc rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "ns": NS}
)

# Visualize the results
print("Using sparql: ")
for r in g.query(q1):
    print(r.sc)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[40]:


# TO DO

# rdflib
print("RDFLib - Person:")
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  print(s)
print("RDFLib - SC of Person:")
for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  for ssc,psc,osc in g.triples((None, RDF.type, s)):
    print(ssc)

# sparql
q2 = prepareQuery('''
  SELECT ?ind WHERE { 
    {?ind a ns:Person.}
    UNION
    {?sc rdfs:subClassOf ns:Person.
     ?ind a ?sc}
  }
  ''',
  initNs = { "ns": NS}
)

# Visualize the results
print("SPARQL:")
for r in g.query(q2):
    print(r.ind)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[48]:


# TO DO

# rdflib
print("RDFLib - Person:")
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  for i,pi,oi in g.triples((s, None, None)):
      print(s,pi,o)
for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  for ssc,psc,osc in g.triples((None, RDF.type, s)):
    for i,pi,oi in g.triples((ssc, None, None)):
      print(ssc,pi,s)

# sparql
q3 = prepareQuery('''
  SELECT ?ind ?p ?c WHERE {
  {
    ?ind a ns:Person.
    ?ind a ?c .
    ?ind ?p ?o .
  } UNION {
    ?c rdfs:subClassOf ns:Person .
    ?ind a ?c .
    ?ind ?p ?o
  }
  }
  ''',
  initNs = { "ns": NS}
)

# Visualize the results
print("SPARQL:")
for r in g.query(q3):
    print(r.ind, r.p, r.c)

