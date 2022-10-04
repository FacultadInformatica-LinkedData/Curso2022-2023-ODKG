
"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/rdf/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

from rdflib.plugins.sparql import prepareQuery

NS = Namespace("http://somewhere#")


q1 = prepareQuery('''
  SELECT ?Subject WHERE { 
    ?Subject rdfs:subClassOf ns:Person. 
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": NS}
)

for r in g.query(q1):
  print(r.Subject)

for s,p,o in g.triples((None, RDFS.subClassOf, NS.Person)):
  print(s)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**

"""

from rdflib.plugins.sparql import prepareQuery

NS = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

q2 = prepareQuery('''
  SELECT ?Subject WHERE { 
    {?Subject rdf:type ns:Person.} UNION
    {?x rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?x.}

  }
  ''',
  initNs = { "rdfs": RDFS, "ns": NS}
)

for r in g.query(q2):
  print(r.Subject)

from rdflib import RDF
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  print(s)
for s,p,o in g.triples((None, RDFS.subClassOf*, NS.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    print(s1)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**

"""

q3 = prepareQuery('''
  SELECT ?Subject ?p ?v WHERE { 
    {?Subject rdf:type ns:Person.
    ?Subjct ?p ?v}
    UNION
    {?x rdfs:subClassOf* ns:Person.
    ?Subject rdf:type ?x.
    ?Subjct ?p ?v}
  }
  ''',
  initNs = { "rdfs": RDFS, "ns": NS}
)

for r in g.query(q3):
  print(r.Subject, r.p, r.v)

from rdflib import RDF
for s,p,o in g.triples((None, RDF.type, NS.Person)):
  for s1,p1,o1 in g.triples((s, None, None)):
    print(s1,p1,o1)
for s,p,o in g.triples((None, RDFS.subClassOf*, NS.Person)):
  for s1,p1,o1 in g.triples((None, RDF.type, s)):
    for s2,p2,o2 in g.triples((s1, None, None)):
      print(s2,p2,o2)
