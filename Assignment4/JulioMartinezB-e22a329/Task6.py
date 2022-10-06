github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

"""Leemos el fichero RDF de la forma que lo hemos venido haciendo"""

from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS
g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

"""Create a new class named Researcher"""

ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

"""**TASK 6.1: Create a new class named "University" **"""

print("")
print("Task 6.1:")
g.add((ns.University, RDF.type, RDFS.Class))
for subj, pred, obj in g.triples((ns.University, None , None)):
    print(subj, pred, obj) 

"""**TASK 6.2: Add "Researcher" as a subclass of "Person"**"""

print("")
print("Task 6.2:")
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for subj, pred, obj in g.triples((ns.Researcher, None , None)):
    print(subj, pred, obj) 

"""**TASK 6.3: Create a new individual of Researcher named "Jane Smith"**"""

print("")
print("Task 6.3:")
g.add((ns.JaneSmith, RDF.type, ns.Researcher))
for subj, pred, obj in g.triples((ns.JaneSmith, None , None)):
    print(subj, pred, obj) 

"""**TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**"""

print("")
print("Task 6.4:")
fullName = Literal("Jane Smith")
given = Literal("Jane")
full = Literal("Smith")
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0/")
g.add((ns.JaneSmith, vcard.FN, fullName))
g.add((ns.JaneSmith, vcard.Given, given))
g.add((ns.JaneSmith, vcard.Family, full))
for subj, pred, obj in g.triples((ns.JaneSmith, None , None)):
    print(subj, pred, obj) 

"""**TASK 6.5: Add UPM as the university where John Smith works**"""

print("")
print("Task 6.5:")
g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.JohnSmith, ns.WorksAt, ns.University))
for subj, pred, obj in g.triples((ns.JohnSmith, None , None)):
    print(subj, pred, obj) 
