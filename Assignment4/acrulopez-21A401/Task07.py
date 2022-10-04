#!/usr/bin/env python
# coding: utf-8

# **Task 07: Querying RDF(s)**

# In[1]:


get_ipython().system("pip install rdflib")
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"


# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# In[2]:


from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

g = Graph()
g.namespace_manager.bind("ns", Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind(
    "vcard", Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False
)
g.parse(github_storage + "/rdf/example6.rdf", format="xml")


# In[8]:


for s, p, o in g:
    print(s, p, o)


# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# In[11]:


from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

q1 = prepareQuery(
    """
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person . 
  }
  """,
    initNs={"rdfs": RDFS, "ns": ns},
)


# Visualize the results
for r in g.query(q1):
    print(r.Subject)


# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
#

# In[13]:

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for ss, pp, oo in g.triples((None, RDF.type, s)):
        print(ss)

for s, p, o in g.triples((None, RDF.type, ns.Person)):
    print(s)


q2 = prepareQuery(
    """
  SELECT ?individuals WHERE { 
    { 
        ?individuals rdf:type ns:Person .
    }
    UNION
    {
        ?subclasses rdfs:subClassOf* ns:Person . 
        ?individuals rdf:type ?subclasses .
    }
  }
  """,
    initNs={"vcard": VCARD, "rdf": RDF, "rdfs": RDFS, "ns": ns},
)


# Visualize the results
for r in g.query(q2):
    print(r.individuals)


# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
#

# In[14]:

for s, p, o in g.triples((None, RDF.type, ns.Person)):
    for ss, pp, oo in g.triples((s, None, None)):
        print(ss, pp)

for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    for ss, pp, oo in g.triples((None, RDF.type, s)):
        for sss, ppp, ooo in g.triples((ss, None, None)):
            print(sss, ppp)

q3 = prepareQuery(
    """
  SELECT ?individuals ?b ?c WHERE { 
    { 
        ?individuals rdf:type ns:Person
    }
    UNION
    {
        ?subclasses rdfs:subClassOf* ns:Person . 
        ?individuals rdf:type ?subclasses
    }
    ?individuals ?b ?c
  }
  """,
    initNs={"vcard": VCARD, "rdf": RDF, "rdfs": RDFS, "ns": ns},
)


# Visualize the results
for r in g.query(q3):
    print(r.individuals, r.b, r.c)
