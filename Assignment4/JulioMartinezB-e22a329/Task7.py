github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example6.rdf", format="xml")

"""**TASK 7.1: List all subclasses of "Person" with RDFLib and SPARQL**"""

#RDFLib
print("")
print("") 
print("Task 7.1")
print("")
print("RDFLib:")
ns=Namespace("http://somewhere#")
for subj,pred,obj in g.triples((None, RDFS.subClassOf,ns.Person)):
    print(subj)

# SPARQL 
print("")
print("SPARQL:")
from rdflib.plugins.sparql import prepareQuery

q1 = prepareQuery('''
  SELECT 
    ?subj
  WHERE { 
    ?subj  rdfs:subClassOf/rdfs:subClassOf*  ns:Person. 
  }
  ''', initNs = { "ns": ns,"rdfs":RDFS}
)
for p in g.query(q1):
    print(p)

"""**TASK 7.2: List all individuals of "Person" with RDFLib and SPARQL (remember the subClasses)**"""

#RDFLib
print("")
print("")
print("Task 7.2")
print("")
print("RDFLib:")

"""for subj in g.subjects(RDF.type,ns.Person):
    print(subj)
  

for subj in g.subjects(RDF.type/RDFS.subClassOf,ns.Person):
    print(subj) """

print("")
print("RDFLib:")

for subj,pred,obj in g.triples((None, RDF.type, ns.Person)):
  print(subj)

for subj,pred,obj in g.triples((None, RDFS.subClassOf, ns.Person)):
  for subj1,pred1,obj1 in g.triples ((None, RDF.type,subj)):
    print(subj1)

#SPARQL
print("")
print("SPARQL:")
q2 = prepareQuery('''
SELECT
?subj 
WHERE {
  ?subj rdf:type/rdfs:subClassOf* ns:Person
}
''',
initNs = {"ns": ns}
)
for p in g.query(q2):
    print(p)

"""**TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**"""

#RDFLib
print("")
print("")
print("Task 7.3")
print("")
print("RDFLib:")
for subj, pred, obj in g.triples((None, RDF.type, ns.Person)):
    for subj1, pred1, obj1 in g.triples((subj, None, None)):
        print(subj1, pred1, obj1)

for subj, pred, obj in g.triples((None, RDFS.subClassOf, ns.Person)):
	for subj1, pred1, obj1 in g.triples((None, RDF.type, subj)):
	    for subj2, pred2, obj2 in g.triples((subj1, None, None)):
        	print(subj2, pred2, obj2)

#SPARQL
print("")
print("SPARQL:")
q3 = prepareQuery('''
SELECT ?subj ?prop ?class
WHERE{
	?subclass rdfs:subClassOf* ns:Person.
	?subj a ?subclass .
	?subj ?prop ?class
}
''',
initNs = {"ns": ns,
	"rdfs":RDFS}
)
for r in g.query(q3):
    print(r)
