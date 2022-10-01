#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[19]:


get_ipython().system('pip install rdflib ')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[20]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[27]:


# TO DO
from rdflib.plugins.sparql import prepareQuery
ns = Namespace("http://somewhere#")
#With RDFLib
for s, p, o in g.triples((None,RDFS.subClassOf,ns.Person)):
    print (s)
print(g.value(subject=None,predicate=RDFS.subClassOf,object=s))
#With Sparql
q1 = prepareQuery('''
    SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf/rdfs:subClassOf* ns:Person .
    }
    ''',initNs = { "ns": ns})
for r in g.query(q1):
    print(r)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[30]:


# TO DO
#With SPARQL
q2 = prepareQuery('''
    SELECT ?Subject WHERE { 
        ?Subject rdf:type/rdfs:subClassOf* ns:Person 
    }
    ''',initNs = { "ns": ns})
for r in g.query(q2):
    print(r)
#With RDFLib
ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None,RDF.type,ns.Person)):
    print (s)
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1,p1,o1 in g.triples((None, RDF.type, s)):
        print(s1)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[38]:


# TO DO
#With SPARQL
q3 = prepareQuery('''
    SELECT ?s ?p ?o WHERE { 
        ?s rdf:type/rdfs:subClassOf* ns:Person .
        ?s ?p ?o 
      }
      ''',initNs = { "ns": ns})
for r in g.query(q3):
    print(r)
#With RDFLib\n",
for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for s1, p1, o1 in g.triples((s, None, None)):
        print(s1, p1, o1)
for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for s1, p1, o1 in g.triples((None, RDFS.subClassOf, s)):
        for s2, p2, o2 in g.triples((s1, None, None)):
            print(s2, p2, o2)

