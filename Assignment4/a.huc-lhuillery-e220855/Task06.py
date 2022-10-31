#!/usr/bin/env python
# coding: utf-8

# **Task 06: Modifying RDF(s)**

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
g.parse(github_storage+"/rdf/example5.rdf", format="xml")


# Create a new class named Researcher

# In[3]:


ns = Namespace("http://somewhere#")

g.add((ns.Researcher, RDF.type, RDFS.Class))

for s, p, o in g:
  print(s,p,o)


# **TASK 6.1: Create a new class named "University"**
# 

# In[4]:


# TO DO
# Visualize the results

g.add((ns.University, RDF.type, RDFS.Class))

for s, p, o in g:
  print(s,p,o)


# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# In[5]:


# TO DO
# Visualize the results

g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

for s, p, o in g:
  print(s,p,o)


# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# In[6]:


# TO DO
# Visualize the results

g.add((ns.JaneSmith, RDF.type, ns.Researcher))

for s, p, o in g:
  print(s,p,o)


# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

# In[7]:


# TO DO
# Visualize the results

VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")

g.add((ns.JaneSmith, VCARD.FN, Literal("Jane Smith")))
g.add((ns.JaneSmith, VCARD.Given, Literal("Jane")))
g.add((ns.JaneSmith, VCARD.Family, Literal("Smith")))

for s, p, o in g:
  print(s,p,o)


# **TASK 6.5: Add UPM as the university where John Smith works**

# In[8]:


# TO DO
# Visualize the results

g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, VCARD.work, ns.UPM))

for s, p, o in g:
  print(s,p,o)


# In[ ]:




