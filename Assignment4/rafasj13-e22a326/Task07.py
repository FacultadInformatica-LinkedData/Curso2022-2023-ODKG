#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[4]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[202]:


# TO DO
ns = Namespace("http://somewhere#")


q1 = prepareQuery('''
  SELECT ?subcls WHERE { 
    ?subcls rdfs:subClassOf+ ns:Person 
  }
  ''', initNs = {
      "ns":ns,
      "rdfs":RDFS
  }
)

# Visualize the results
for r in g.query(q1):
    print(r.subcls)


# In[203]:


for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s,p,o)
    for s1,p1,o1 in g.triples((None, p, s)):
        print(s1,p1,o1)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[204]:


for s,p1,o in g.triples((None, RDF.type, ns.Person)):
        print(s,p,o)
        
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1,p1,o1 in g.triples((None, RDF.type, s)):
        print(s1,p1,o1)

# Visualize the results


# In[205]:


q2 = prepareQuery('''
  SELECT  ?names WHERE { 
    ?class rdfs:subClassOf* ns:Person .
    ?names a ?class .
  }
  ''', initNs = {
      "ns":ns,
      "rdfs":RDFS,
  }
)

# Visualize the results
for r in g.query(q2):
    print(r.names)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[206]:


q3 = prepareQuery('''
  SELECT ?names ?prop ?val WHERE { 
    ?cls rdfs:subClassOf* ns:Person .
    ?names a ?cls .
    ?names ?prop ?val 
    
  }
  ''', initNs = {
      "ns":ns,
      "rdfs":RDFS,
  }
)

# Visualize the results
for r in g.query(q3):
  print(r.names, r.prop, r.val)
# Visualize the results


# In[207]:


def individuals_and_prop(sub, prop, cls):
    for s1, p1, o1 in g.triples((sub, prop, cls)):
        for s2, p2, o2 in g.triples((s1, None, None)):
            print(s2,p2,o2)

            
individuals_and_prop(None, RDF.type, ns.Person)           
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    individuals_and_prop(None, RDF.type, s)


# In[ ]:




