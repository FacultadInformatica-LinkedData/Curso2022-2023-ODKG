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

# In[17]:


# TO DO
# Visualize the results
from rdflib.plugins.sparql import prepareQuery

##########################################################################################
#  USING RDFLib
##########################################################################################
from rdflib import XSD
ns = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)
    for s1,p1,o1 in g.triples((None, RDFS.subClassOf, s)):
        print(s1)
##########################################################################################
#  USING SPARQL
##########################################################################################
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")


q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf+ ns:Person. 
  }
  ''',
  initNs = { "rdfs": RDFS, 
            "ns" : ns}
)
for r in g.query(q1):
    print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[30]:


# TO DO
# Visualize the results
##########################################################################################
#  USING RDFLib
##########################################################################################
ns = Namespace("http://somewhere#")
for s,p,o in g.triples((None, RDF.type, ns.Person)):
    print(s)
for s,p,o in g.triples((None, RDF.type, ns.Researcher)):
    print(s)
##########################################################################################
#  USING SPARQL
##########################################################################################
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")


q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
      ?class rdfs:subClassOf* ns:Person. 
    ?Subject a ?class. 
  }
  ''',
  initNs = { "rdf": RDF,
            "rdfs": RDFS,
            "ns" : ns}
)
for r in g.query(q1):
    print(r)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[59]:


# TO DO
# Visualize the results
##########################################################################################
#  USING RDFLib
##########################################################################################
ns = Namespace("http://somewhere#")

nsclass = ns.Person
nsclassant = 0
while (nsclassant!= nsclass):
    nsclassant = nsclass
    for s,p,o in g.triples((None, RDF.type, nsclass)):
        for s1,p1,o1 in g.triples((s, None,None)):
            print(s1,p1,o1)
    for s2, p2, o2 in g.triples((None, RDFS.subClassOf, nsclass)):
        nsclass = s2
# for s,p,o in g.triples((None, RDF.type, ns.Researcher)):
#     print(s)

##########################################################################################
#  USING SPARQL
##########################################################################################
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")


q1 = prepareQuery('''
  SELECT ?Subject ?prop ?value WHERE { 
      ?class rdfs:subClassOf* ns:Person. 
    ?Subject a ?class. 
    ?Subject ?prop ?value
  }
  ''',
  initNs = { "rdf": RDF,
            "rdfs": RDFS,
            "ns" : ns}
)
for r in g.query(q1):
    print(r)

