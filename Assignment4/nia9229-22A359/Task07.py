#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[3]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[4]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[21]:


ns = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": ns}
)
for r in g.query(q1):
  print(r.Subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[36]:


for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2,p2,o2 in g.triples((None, RDF.type, s)):
        print(s2)
        
q2 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Class rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?Class.
  }
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns}
)
for r in g.query(q2):
  print(r.Subject)
# Visualize the results


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[38]:


for s,p,o in g.triples((None, RDF.type, ns.Person)):
    for s2,p2,o2 in g.triples((s, None, None)):
      print(s2,p2,o2)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s2,p2,o2 in g.triples((None, RDF.type, s)):
        for s3,p3,o3 in g.triples((s2, None, None)):
            print(s3,p3,o3)

q3 = prepareQuery('''
  SELECT ?Subject ?Predicate ?Object WHERE { 
    ?Class rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?Class.
    ?Subject ?Predicate ?Object
  }
  ''',
  initNs = { "rdf": RDF, "rdfs": RDFS, "ns": ns}
)
for r in g.query(q3):
  print(r.Subject, r.Predicate, r.Object)
# Visualize the results


# In[ ]:




