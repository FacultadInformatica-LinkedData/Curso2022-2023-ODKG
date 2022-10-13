#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[6]:


from rdflib import Graph, Namespace, Literal
from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

ns = Namespace("http://somewhere#")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[9]:


# RDFLib
print('RDFLib: List all subclasses of "Person".')
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)


# In[8]:


# SPARQL
q1 = prepareQuery('''
    SELECT ?Subclass WHERE { 
        ?Subclass rdfs:subClassOf ns:Person
    }
    ''',
    initNs = { "ns": ns, "rdfs": RDFS }
)

# Visualize the results
for r in g.query(q1):
    print(r.Subclass)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[10]:


# RDFLib
for s,_,_ in g.triples((None, RDF.type, ns.Person)):
    print(s)

for s,_,_ in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1,_,_ in g.triples((None, RDF.type, s)):
        print(s1)


# In[12]:


# SPARQL
q2 = prepareQuery('''
    SELECT ?Person WHERE { 
        ?Person a|(a/rdfs:subClassOf) ns:Person
    }
    ''',
    initNs = { "ns": ns, "rdfs": RDFS }
)

for r in g.query(q2):
    print(r.Person)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[15]:


#RDFLib
def getRecursive(x):
    for s1,_,_ in g.triples((None, RDFS.subClassOf, x)):
        for s2,_,_ in g.triples((None, RDF.type, s1)):
            for s3,p3,o3 in g.triples((s2, None, None)):
                print(s3,p3,o3)
        getRecursive(s1)

for s1,_,_ in g.triples((None, RDF.type, ns.Person)):
    for s2,p2,o2 in g.triples((s1, None, None)):
        print(s2,p2,o2)

getRecursive(ns.Person)


# In[16]:


# SPARQL
q3 = prepareQuery('''
    SELECT ?Person ?Prop ?Value WHERE { 
        ?Person a|(a/rdfs:subClassOf) ns:Person .
    ?Person ?Prop ?Value
    }
    ''', 
    initNs = { "ns": ns, "rdfs": RDFS }
    )

for r in g.query(q3):
    print(r.Person, r.Prop, r.Value)

