# Hands-on assignment 4 - Self assessment #

## Checklist ##

**General Goals**

- [ ] Transform data into RDF.
- [ ] Define RML mappings for the data.
- [ ] Transform the data into RDF.

**For each dataset:**

**RML file with the mappings**

- [ ] “*.rml” under an “mappings” directory.

**A YML file with the mapping rules (optional)**

- [ ] “*.yml” under an “mappings” directory.

**RDF file in the Turtle syntax with the data transformed into RDF**

- [ ] “*.ttl” under an “rdf” directory.

**SPARQL file with queries to verify your data**

- [ ] “queries.sparql” under an “rdf” directory.

**A Markdown document with the hands-on self-assessment**

- [ ] “selfAssessmentHandsOn4.md” in the root of the group directory.


**Every RDF file:**

- [ ] Uses the .ttl extension
- [ ] Is serialized in the Turtle format
- [ ] Follows the resource naming strategy
- [ ] Uses class and property URIs that are the same as those used in the ontology

**Every URI in the RDF files:**

- [ ] Is "readable" and has some meaning (e.g., it is not an auto-increased integer)
- [ ]  Is not encoded as a string
- [ ]  Does not contain a double slash (i.e., “//”)

**Every individual in the RDF files:**

- [ ]  Has a label with the name of the individual
- [ ]  Has a type

**Every value in the RDF files:**
- [ ]  Is trimmed
- [ ]  Is properly encoded (e.g., dates, booleans)
- [ ]  Includes its datatype
- [ ]  Uses the correct datatype (e.g., values of 0-1 may be booleans and not integers, not every string made of numbers is a number)


## Comments on self-assessment ##

Previous updates made as some typo errors found