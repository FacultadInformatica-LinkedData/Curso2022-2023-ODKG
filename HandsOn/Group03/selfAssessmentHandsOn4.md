# Hands-on assignment 4 - Self assessment #

## Checklist ##

**General Goals**

- [ ] Transform data into RDF.
- [ ] Define RML mappings for the data.
- [ ] Transform the data into RDF.

**For each dataset:**

**RML file with the mappings**

- [x] “*.rml” under an “mappings” directory.

**A YML file with the mapping rules (optional)**

- [x] “*.yml” under an “mappings” directory.

**RDF file in the Turtle syntax with the data transformed into RDF**

- [x] “*.ttl” under an “rdf” directory.

**SPARQL file with queries to verify your data**

- [ ] “queries.sparql” under an “rdf” directory.

**A Markdown document with the hands-on self-assessment**

- [x] “selfAssessmentHandsOn4.md” in the root of the group directory.


**Every RDF file:**

- [x] Uses the .ttl extension
- [x] Is serialized in the Turtle format
- [x] Follows the resource naming strategy
- [x] Uses class and property URIs that are the same as those used in the ontology

**Every URI in the RDF files:**

- [X] Is "readable" and has some meaning (e.g., it is not an auto-increased integer)
- [X]  Is not encoded as a string
- [X]  Does not contain a double slash (i.e., “//”)

**Every individual in the RDF files:**

- [X]  Has a label with the name of the individual
- [X]  Has a type

**Every value in the RDF files:**
- [X]  Is trimmed
- [X]  Is properly encoded (e.g., dates, booleans)
- [X]  Includes its datatype
- [X]  Uses the correct datatype (e.g., values of 0-1 may be booleans and not integers, not every string made of numbers is a number)


## Comments on self-assessment ##

Previous updates made as some typo errors found & notebook used upload