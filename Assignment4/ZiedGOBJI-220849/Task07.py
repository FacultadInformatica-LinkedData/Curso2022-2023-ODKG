# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

# %% [markdown]
# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# %% [markdown]
# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# %%
# TO DO
from rdflib.plugins.sparql import prepareQuery 


ns = Namespace("http://somewhere#")

# find all subjects (s) of type (rdfs:subclassof) person (rdf:Person)
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
    print(s)

q1=prepareQuery("SELECT DISTINCT ?s WHERE {?s rdfs:subClassOf ns:Person}", initNs = { "rdfs": RDFS, "ns": ns}
)


for r in g.query(q1):
  print(r.s)

# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
    print(s)

for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s_sub,p_sub,o_sub in g.triples((None, RDF.type, s)):
    print(s_sub)

# SPARQL
q_person = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?class rdfs:subClassOf* ns:Person 
    ?Subject a ?class
  }
  ''', initNs = {
      "ns":ns,
      "rdfs":RDFS
  }
)
for r in g.query(q_person):
  print(r)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
"""

# RDFLib
for s,p,o in g.triples((None, RDF.type, ns.Person)):
  for s_property,p_property,o_property in g.triples((s, None, None)):

    print(s_property,p_property,o_property)


for s,p,o in g.triples((None, RDFS.subClassOf, ns.Person)):
  for s_sub,p_sub,o_sub in g.triples((None, RDF.type, s)):
    for s_property,p_property,o_property in g.triples((s_sub, None, None)):

      print(s_property,p_property,o_property)

# SPARQL
q_property = prepareQuery('''
  SELECT ?s ?p ?value WHERE { 
    ?class rdfs:subClassOf* ns:Person 
    ?s a ?class 
    ?s ?p ?value
  }
  ''', initNs = {
      "ns":ns,
      "rdfs":RDFS
  }
)
for r in g.query(q_property):
  print(r.s, r.p, r.o)




