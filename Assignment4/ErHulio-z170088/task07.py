# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
#!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

# %% [markdown]
# Leemos el fichero RDF de la forma que lo hemos venido haciendo

# %%
from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

# %% [markdown]
# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# %%
from rdflib.plugins.sparql import prepareQuery

ns = Namespace("http://somewhere#")
for s, p, o in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(s)

print()

q1 = prepareQuery('''
  SELECT 
    ?Subject
  WHERE {
    ?Subject rdfs:subClassOf ns:Person.
  }  
  ''',
  initNs = { "rdfs": RDFS, "ns":ns}
)

for q in g.query(q1):
  print(q.Subject)

# %% [markdown]
# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**
# 

# %%
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  print(s)

for s, p, o in g.triples((None, RDF.type, ns.Researcher)):
  print(s)

print()

q2 = prepareQuery('''
  SELECT 
    ?Subject ?Subject2
  WHERE {
    ?Subject rdf:type ns:Person.
    ?Subject2 rdf:type ns:Researcher.
  }  
  ''',
  initNs = { "rdf": RDF, "ns":ns}
)

for q in g.query(q2):
  for r in q:
    print(r)

# %% [markdown]
# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# %%
for s, p, o in g.triples((None, RDF.type, ns.Person)):
  for w, x, y in g.triples((s, None, None)):
    print(s, x, y)

for s, p, o in g.triples((None, RDF.type, ns.Researcher)):
  for w, x, y in g.triples((s, None, None)):
    print(s, x, y)

print()

q3 = prepareQuery('''
  SELECT 
    ?Subject ?Predicate ?Object ?Subject2 ?Predicate2 ?Object2
  WHERE {
    ?Subject rdf:type ns:Person.
    ?Subject ?Predicate ?Object.

    ?Subject2 rdf:type ns:Researcher.
    ?Subject2 ?Predicate2 ?Object2.
  }  
  ''',
  initNs = { "rdf": RDF, "ns":ns}
)

for q in g.query(q3):
    print(q.Subject, q.Predicate, q.Object)
    print(q.Subject2, q.Predicate2, q.Object2)


