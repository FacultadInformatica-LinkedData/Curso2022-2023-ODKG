github_storage = "https://raw.githubusercontent.com/FacultadInformatica-LinkedData/Curso2021-2022/master/Assignment4/course_materials/"

from rdflib import Graph, Namespace, Literal, URIRef
g1 = Graph()
g2 = Graph()
g3 = Graph()
g1.parse(github_storage+"rdf/data03.rdf", format="xml")
g2.parse(github_storage+"rdf/data04.rdf", format="xml")

"""Busca individuos en los dos grafos y enlázalos mediante la propiedad OWL:sameAs, inserta estas coincidencias en g3. Consideramos dos individuos iguales si tienen el mismo apodo y nombre de familia. Ten en cuenta que las URI no tienen por qué ser iguales para un mismo individuo en los dos grafos."""

from rdflib.namespace import RDF, OWL, RDFS
from rdflib.plugins.sparql import prepareQuery
nsg1 = Namespace("http://data.three.org#")
nsg2 = Namespace ("http://data.four.org#")
VCARD = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

def checkApodo(refInstance, refGraph, compInstance, compGraph):
  return refGraph.value(refInstance, VCARD.Given, None) == compGraph.value(compInstance, VCARD.Given, None)

def  checkFamilia(refInstance, refGraph, compInstance, compGraph):
  return refGraph.value(refInstance, VCARD.FN, None) == compGraph.value(compInstance, VCARD.FN, None)

def checkCoincidence(refInstance, refGraph, compInstance, compGraph):
  return checkApodo(refInstance, refGraph, compInstance, compGraph) and checkFamilia(refInstance, refGraph, compInstance, compGraph)



for refIndividual, prop1, val in g1.triples((None, RDF.type, nsg1.Person)):
  for compIndividual, prop2, val in g2.triples((None, RDF.type, nsg2.Person)):
    if checkCoincidence(refIndividual, g1, compIndividual, g2):
      g3.add((refIndividual, OWL.sameAs, compIndividual))

queryGetAllInd = prepareQuery("""
  SELECT ?person1 ?sameas ?person2 WHERE{    
      ?person1 ?sameas ?person2.
  }
""")
for r in g3.query(queryGetAllInd):
  print(r)