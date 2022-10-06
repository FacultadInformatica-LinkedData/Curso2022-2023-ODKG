#!/usr/bin/env python
# coding: utf-8

# **Task 08: Completing missing data**

# In[18]:


github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# In[19]:


from rdflib import Graph, Namespace, Literal, URIRef
from rdflib.namespace import RDF, RDFS
from rdflib.plugins.sparql import prepareQuery

g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")


# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# In[20]:



def complete_fields(g1, g2, sub, prop, cls):
    for s, p, o in g2.triples((sub, prop, cls)):
        g1.add((sub, p, o))


dat = Namespace("http://data.org#")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

properties = [vcard.Given, vcard.Family, vcard.EMAIL]


# In[21]:





print("graph 1 previous")
for s, p, o in g1.triples((None, RDF.type, dat.Person)):
    for s1, p1, o1 in g1.triples((s, None, None)):
        print(s1, p1, o1)
        

for s, p, o in g1.triples((None, RDF.type, dat.Person)):
    for fn_prop in properties:
        complete_fields(g1, g2, s, fn_prop, None)


print("graph 1 after")
for s, p, o in g1.triples((None, RDF.type, dat.Person)):
    for s1, p1, o1 in g1.triples((s, None, None)):
        print(s1, p1, o1)

