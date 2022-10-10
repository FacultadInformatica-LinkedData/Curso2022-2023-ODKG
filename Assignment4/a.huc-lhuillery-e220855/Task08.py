#!/usr/bin/env python
# coding: utf-8

# **Task 08: Completing missing data**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# In[2]:


from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g1.parse(github_storage+"/rdf/data01.rdf", format="xml")
g2.parse(github_storage+"/rdf/data02.rdf", format="xml")


# Tarea: lista todos los elementos de la clase Person en el primer grafo (data01.rdf) y completa los campos (given name, family name y email) que puedan faltar con los datos del segundo grafo (data02.rdf). Puedes usar consultas SPARQL o iterar el grafo, o ambas cosas.

# In[3]:


from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns = Namespace("http://data.org#")

personnes = prepareQuery('''
  SELECT ?individu ?prop ?obj WHERE { 
    { 
        ?individu rdf:type ns:Person .
        ?individu ?prop ?obj
    }
    UNION 
    {
        ?individu rdf:type ?subClass.
        ?subClass rdfs:subClassOf ns:Person.
        ?individu ?prop ?obj
    }
  }
  ''',
  initNs = { "vcard": VCARD , "ns": ns , "rdf": RDF}

)

print("Data 1 :")
for r in g1.query(personnes):
  print(r.individu, r.prop, r.obj)

print("Data 2 :")
for r in g2.query(personnes):
  print(r.individu, r.prop, r.obj)


# In[4]:


for r in g2.query(personnes):
    g1.add((r.individu, r.prop, r.obj))

print("Data 1 :")
for r in g1.query(personnes):
  print(r.individu, r.prop, r.obj)


# In[ ]:




