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
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0/"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[3]:


# TO DO
# Visualize the results

from rdflib.plugins.sparql import prepareQuery

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
ns = Namespace("http://somewhere#")

q1 = prepareQuery('''
  SELECT ?subClass WHERE { 
     ?subClass rdfs:subClassOf ns:Person.
  }
  ''',
  initNs = {"ns" :ns , "rdfs" : RDFS}
)

for r in g.query(q1):
  print(r.subClass)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# In[4]:


# TO DO
# Visualize the results

q2 = prepareQuery('''
  SELECT ?individu WHERE { 
    { 
        ?individu rdf:type ns:Person.
    }
    UNION 
    {
        ?individu rdf:type ?subClass.
        ?subClass rdfs:subClassOf ns:Person.
    }
  }
  ''',
  initNs = { "vcard": VCARD , "ns": ns , "rdf": RDF}

)

for r in g.query(q2):
  print(r.individu)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# In[5]:


# TO DO
# Visualize the results 

q3 = prepareQuery('''
  SELECT ?individu ?prop ?obj WHERE { 
      {
        ?individu rdf:type ns:Person.
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

for r in g.query(q3):
  print(r.individu, r.prop, r.obj)


# In[ ]:




