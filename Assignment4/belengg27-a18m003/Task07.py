#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

for s,p,o in g: 
  print(s,p,o)


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[3]:


# RDFLib
ns = Namespace("http://somewhere#")    

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)


# In[4]:


# SPARQL
from rdflib.plugins.sparql import prepareQuery

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

# In[5]:


# RDFLib

# Individuals of "Person"
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)

# Individuals of the subclases of "Person"
for subclass,_,_ in g.triples((None, RDFS.subClassOf, ns.Person)):
    for ind,_,_ in g.triples((None, RDF.type, subclass)):
        print(ind)


# In[6]:


# SPARQL

q2 = prepareQuery('''
  SELECT ?ind WHERE { 
    {
    ?ind RDF:type ns:Person . 
    } UNION {
    ?s RDFS:subClassOf* ns:Person .
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

# In[7]:


# RDFLib
# Individuals of "Person"
for s1,p1,o1 in g.triples((None, RDF.type, ns.Person)):
    for s2,p2,o2 in g.triples((s1, None, None)):
        print(s2, p2)

# Individuals of the subclases of "Person"
for s1,p1,o1 in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2,p2,o2 in g.triples((None, RDF.type, s1)):
        for s3,p3,o3 in g.triples((s2, None, None)):
            print(s3,p3)


# In[8]:


# SPARQL
q3 = prepareQuery('''
  SELECT ?ind ?prop WHERE { 
    {
    ?ind RDF:type ns:Person . 
    } UNION {
    ?s RDFS:subClassOf* ns:Person .
    ?ind RDF:type ?s .
    }
    ?ind ?prop ?obj
  }
  ''',
  initNs = {"RDF":RDF, "RDFS":RDFS, "ns": ns}
)


# Visualize the results
for r in g.query(q3):
 print(r.ind, r.prop)

