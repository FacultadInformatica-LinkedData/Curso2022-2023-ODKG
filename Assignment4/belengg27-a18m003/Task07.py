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

# In[13]:


from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?s WHERE { 
    ?s RDFS:subClassOf ns:Person . 
  }
  ''',
  initNs = {"RDFS":RDFS, "ns": ns}
)


# Visualize the results
for r in g.query(q1):
 print(r.s)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[18]:


q2 = prepareQuery('''
  SELECT ?ind WHERE { 
    {
    ?ind RDF:type ns:Person . 
    } UNION {
    ?s RDFS:subClassOf ns:Person .
    ?ind RDF:type ?s .
    }
  }
  ''',
  initNs = {"RDF":RDF, "RDFS":RDFS, "ns": ns}
)


# Visualize the results
for r in g.query(q2):
 print(r.ind)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[25]:


q3 = prepareQuery('''
  SELECT ?ind ?prop ?s WHERE { 
    {
    ?ind RDF:type ns:Person . 
    } UNION {
    ?s RDFS:subClassOf ns:Person .
    ?ind RDF:type ?prop .
    }
    ?ind ?prop ?s .
  }
  ''',
  initNs = {"RDF":RDF, "RDFS":RDFS, "ns": ns}
)


# Visualize the results
for r in g.query(q3):
 print(r.ind, r.prop, r.s)

