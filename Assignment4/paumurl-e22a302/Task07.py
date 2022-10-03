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
from rdflib.plugins.sparql import prepareQuery
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")
ns = Namespace("http://somewhere#")


# In[3]:


for s,p,o in g.triples((None, None, None)):
  print(s,p,o)


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[4]:


# TO DO
# Visualize the results
#RDFLib
print("Consulta RDFLib:")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)


print("\n")

#SPARQL
print("Consulta SPARQL:")
q1 = prepareQuery('''
  SELECT ?subject WHERE { 
    ?subject rdfs:subClassOf ns:Person .
  } 
  ''',
  initNs = { "rdfs": RDFS, "ns":ns}
)

for r in g.query(q1):
  print(r.subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[5]:


# TO DO
# Visualize the results
# TO DO
# Visualize the results
#RDFLib
print("Consulta RDFLib:")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for sub,p1,o1 in g.triples((None,RDFS.subClassOf,ns.Person)):
    for s2,p2,o2 in g.triples((None,RDF.type,sub)):
        print(s2)

print("\n")
#SPARQL
print("Consulta SPARQL:")
q2 = prepareQuery('''
  SELECT ?ins WHERE { 
    ?ins rdf:type/rdfs:subClassOf* ns:Person .

  } 
  ''',
  initNs = { "rdf": RDF, "ns":ns}
)

for r in g.query(q2):
  print(r.ins)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[6]:


# TO DO
# Visualize the results
#RDFLib
print("Consulta RDFLib:")
for s,p,o in g.triples((None,RDF.type,ns.Person)):
  for s2,p2,o2 in g.triples((s,None,None)):
    print(s2,p2,o2)
    
for s,p,o in g.triples((None,RDFS.subClassOf,ns.Person)):
  for s2,p2,o2 in g.triples((None,RDF.type,s)):
    for s3,p3,o3 in g.triples((s2,None,None)):
        print(s3,p3,o3)
    
print("\n")

#SPARQL
print("Consulta SPARQL:")
q3 = prepareQuery('''
  SELECT ?ins ?prop ?ob WHERE { 
    ?ins rdf:type/rdfs:subClassOf* ns:Person .
    ?ins ?prop ?ob .

  } 
  ''',
  initNs = { "rdf": RDF, "ns":ns}
)

for r in g.query(q3):
  print(r.ins,r.prop,r.ob)

