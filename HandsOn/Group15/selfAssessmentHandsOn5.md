# Hands-on assignment 5 - Self assessment #

## Checklist ##

**A JSON file with the operations performed over the data for linking them**
- [X] “*-with-links.json” under a “lodrefine” directory

**A CSV file with the updated versions of the datasets**
- [X] “*-with-links.csv” under a “csv” directory

**An RML file with the updated versions of the mappings**
- [X] “*-with-links.rml” under a “mappings” directory

**An RDF file in the Turtle syntax with the data transformed into RDF**
- [X] “*-with-links.ttl” under an “rdf” directory
- [X] Contains at least one owl:sameAs property

**A SPARQL file with queries to verify your links**
- [X] “queries-with-links.sparql” under an “rdf” directory
- [X] Includes at least 1 query
- [X] Contains queries that retrieve the data that would be needed in the application
- [X] Every query makes use of the ontology
- [X] Every query returns a non-empty result
- [X] Every query makes use of the owl:sameAs links


## Comments on self-assessment ##
The dataset that we used is about bus stops in Alcobendas, a district of Community of Madrid. As the dataset is small and the values of the data are similar, we have found only 61 of 427 data(column street_name) that can be linked to wikidata. Although we have tried to clean the values by replacing abbreviations, such as replacing "Avda" by "Avenida", "Ctra" by "Carretera", we only got some incorrect links. 