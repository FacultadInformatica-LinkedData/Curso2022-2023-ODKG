# %% [markdown]
# **Task 07: Querying RDF(s)**

# %%
!pip install rdflib 
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
# 

# %%


# %% [markdown]
# **TASK 7.3: List all individuals of "Person" and all their properties including their class with RDFLib and SPARQL**
# 

# %%



