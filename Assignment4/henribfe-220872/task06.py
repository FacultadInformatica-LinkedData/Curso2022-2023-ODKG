from rdflib import Graph, Namespace, Literal
from rdflib.namespace import RDF, RDFS

github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2020-2021/master/Assignment4"

g = Graph()
g.namespace_manager.bind('ns', Namespace("http://somewhere#"), override=False)
g.namespace_manager.bind('vcard', Namespace("http://www.w3.org/2001/vcard-rdf/3.0#"), override=False)
g.parse(github_storage+"/resources/example5.rdf", format="xml")

ns = Namespace("http://somewhere#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

g.add((ns.Researcher, RDF.type, RDFS.Class))

""" Task 6.1 """
g.add((ns.University, RDF.type, RDFS.Class))

""" Task 6.2 """
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))

""" Task 6.3 """
g.add((ns.JaneSmith, RDF.type, ns.Researcher))

""" Task 6.4 """
g.add((ns.JaneSmith, VCARD.Family, Literal("Smith")))
g.add((ns.JaneSmith, VCARD.Given, Literal("Jane")))
g.add((ns.JaneSmith, VCARD.FN, Literal("Jane Smith")))

""" Task 6.5 """
g.add((ns.UPM, RDF.type, ns.University))
g.add((ns.WorksAt, RDF.type, RDF.Property))
g.add((ns.JohnSmith, ns.WorksAt, ns.UPM))

for s, p, o in g:
  print(s,p,o)
