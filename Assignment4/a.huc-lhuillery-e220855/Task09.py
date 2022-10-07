#!/usr/bin/env python
# coding: utf-8

# **Task 09: Data linking**

# In[1]:


get_ipython().system('pip install rdflib')
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials/"


# In[2]:


from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")


# Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos.

# In[3]:


from rdflib.plugins.sparql import prepareQuery
from rdflib.namespace import RDF, RDFS, OWL

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")
ns1 = Namespace("http://data.three.org#")

personnes1 = prepareQuery('''
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
  initNs = { "vcard": VCARD , "ns": ns1 , "rdf": RDF}
)

ns2 = Namespace("http://data.four.org#")

personnes2 = prepareQuery('''
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
  initNs = { "vcard": VCARD , "ns": ns2 , "rdf": RDF}
)

print("Data 1 :")
for r in g1.query(personnes1):
  print(r.individu, r.prop, r.obj)

print("Data 2 :")
for r in g2.query(personnes2):
  print(r.individu, r.prop, r.obj)


# In[4]:


noms = prepareQuery('''
  SELECT ?individu ?obj WHERE { 
    ?individu vcard:Family ?obj.
  }
  ''',
  initNs = { "vcard": VCARD }
)

prenoms = prepareQuery('''
  SELECT ?individu ?obj WHERE { 
    ?individu vcard:Given ?obj.
  }
  ''',
  initNs = { "vcard": VCARD }
)

for r1 in g1.query(noms):
    for r2 in g2.query(noms):
        if (r1.obj == r2.obj):
            g3.add((r1.individu, OWL.sameAs, r2.individu))
            
g4 = Graph()
for r1 in g1.query(prenoms):
    for r2 in g2.query(prenoms):
        if (r1.obj == r2.obj):
            g4.add((r1.individu, OWL.sameAs, r2.individu))

g3 = (g3 & g4)

D3 = prepareQuery('''
select ?s ?p ?o where {
?s ?p ?o
}''')
print("Data 3 :")
for r in g3.query(D3):
    print(r.s, r.p, r.o)


# In[ ]:




