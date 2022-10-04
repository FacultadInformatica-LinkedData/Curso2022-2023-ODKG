#!/usr/bin/env python
# coding: utf-8

# **Task 08: Completing missing data**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# In[2]:


from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")
ns = Namespace("http://data.org#")


# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# In[3]:


#Vemos que nos falta información respecto al segundo grafo
for s,p,o in g1.triples((None, RDF.type, ns.Person)):
    for s1,p1,o1 in g1.triples((s,None,None)):
      print(s1,p1,o1)


# In[4]:


#Completamos con este grafo, no hay consistencia en los campos que faltan en el primer grafo
for s,p,o in g2.triples((None, RDF.type, ns.Person)):
    for s1,p1,o1 in g2.triples((s,None,None)):
      print(s1,p1,o1)


# In[5]:


#Completamos el primer grafo con todos los datos del segundo
for s,p,o in g2.triples((None, RDF.type, ns.Person)):
    for s1,p1,o1 in g2.triples((s,vcard.Given,None)):
        g1.add((s1,p1,o1))
    for s2,p2,o2 in g2.triples((s,vcard.Family,None)):
        g1.add((s2,p2,o2))
    for s3,p3,o3 in g2.triples((s,vcard.Email,None)):
        g1.add((s3,p3,o3))


# In[6]:


#Vemos los cambios
for s,p,o in g1.triples((None, RDF.type, ns.Person)):
    for s1,p1,o1 in g1.triples((s,None,None)):
      print(s1,p1,o1)
