# %% [markdown]
# **Task 06: Modifying RDF(s)**

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
g.parse(github_storage+"/rdf/example5.rdf", format="xml")

# %% [markdown]
# Create a new class named Researcher

# %%
ns = Namespace("http://somewhere#")
g.add((ns.Researcher, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.1: Create a new class named "University"**
# 

# %%
# TO DO
# Visualize the results
g.add((ns.University, RDF.type, RDFS.Class))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.2: Add "Researcher" as a subclass of "Person"**

# %%
g.add((ns.Researcher, RDFS.subClassOf, ns.Person))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.3: Create a new individual of Researcher named "Jane Smith"**

# %%

g.add((ns.janeSmith, RDF.type, ns.Researcher))
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.4: Add to the individual JaneSmith the fullName, given and family names**

# %%
# TO DO
vcard = Namespace("http://www.w3.org/2001/vcard-rdf/3.0#")

fullName = Literal('Jane Smith')
given = Literal('Jane')
familyNames = Literal('Smith')


g.add((ns.janeSmith, vcard.FN, fullName))
g.add((ns.janeSmith, vcard.Given, given))
g.add((ns.janeSmith, vcard.Family, familyNames))


# visualize
for s, p, o in g:
  print(s,p,o)

# %% [markdown]
# **TASK 6.5: Add UPM as the university where John Smith works**

# %%
# TO DO

# add UPM as a subclass of University
g.add((ns.UPM, RDFS.subClassOf, ns.University))

# add the realtion 'work' between Jane Smith and UPM
g.add((ns.janeSmith, ns.Work, ns.UPM))

for s, p, o in g:
  print(s,p,o)
# Visualize the results


