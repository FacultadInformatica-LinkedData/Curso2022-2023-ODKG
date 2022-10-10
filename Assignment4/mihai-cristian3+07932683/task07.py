# **Task 07: Querying RDF(s)**

!pip install rdflib 
github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

# **TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**

# RDFlib way
from rdflib.namespace import RDF
ns = Namespace("http://somewhere#")

# Visualize the results
print("RDFlib way")
for result11 in g.triples((None, RDFS.subClassOf, ns.Person)):
  print(result11)


# SPARQL way
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery("""
SELECT ?sub WHERE {
  {
    ?sub RDFS:subClassOf+ ns:Person
  }
""", initNs = {
      "ns":ns,
      "RDFS":RDFS
  })

# Visualize the results
print("SPARQL way")
for r1 in g.query(q1):
  print(r1)

# **TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

# RDFlib way
# Visualize the results
print("RDFlib way")
for result21 in g.triples((None, RDF.type, ns.Person)):
  print(result21)
for result22 in g.triples((None, RDFS.subClassOf, ns.Person)):
  for result23 in g.triples((None, RDF.type, result22[0])):
    print(result23)


# SPARQL way
# SPARQL way
q2 = prepareQuery('''
  SELECT ?ind WHERE { 
    ?classInd RDFS:subClassOf* ns:Person . 
    ?ind a ?classInd
  }''',
  initNs = {"RDF":RDF, "RDFS":RDFS, "ns":ns}
)

# Visualize the results
print("SPARQL way")
for r2 in g.query(q2):
  print(r2)

# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

# RDFlib way
# Visualize the results
print("RDFlib way")

for s, p, o in g:
  for result31 in g.triples((None, RDF.type, ns.Person)):
    if(s.eq(result31[0])): 
      print (s, p, o)
  for result32 in g.triples((None, RDFS.subClassOf, ns.Person)):
    for result33 in g.triples((None, RDF.type, result32[0])):
      if(s.eq(result33[0])): 
        print (s, p, o)


# SPARQL way
q3 = prepareQuery('''
  SELECT ?ind ?p ?o WHERE { 
    ?classInd RDFS:subClassOf* ns:Person . 
    ?ind a ?classInd .
    ?ind ?p ?o
  }''',
  initNs = {"RDF":RDF, "RDFS":RDFS, "ns":ns}
)

# Visualize the results
print("SPARQL way")
for r3 in g.query(q3):
  print(r3)