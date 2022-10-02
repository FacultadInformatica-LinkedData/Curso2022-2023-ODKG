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

# In[3]:


from rdflib.plugins.sparql import prepareQuery
q1 = prepareQuery('''
  SELECT ?SubClass WHERE { 
    ?SubClass rdfs:subClassOf ns:Person.
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": Namespace("http://somewhere#")}
)


# Visualize the results

for r in g.query(q1):
  print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[4]:



q2 = prepareQuery('''
  SELECT ?instance WHERE { 
    ?instance a ?type.
    ?type rdfs:subClassOf* ns:Person
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": Namespace("http://somewhere#")}
)


# Visualize the results

for r in g.query(q2):
  print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[5]:



q3 = prepareQuery('''
  SELECT ?instance ?p ?o WHERE { 
    ?instance a ?type.
    ?type rdfs:subClassOf* ns:Person.
    ?instance ?p ?o
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": Namespace("http://somewhere#")}
)


# Visualize the results

for r in g.query(q3):
  print(r)


# In[ ]:




