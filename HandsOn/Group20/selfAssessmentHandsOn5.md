# Hands-on assignment 5 – Self assessment

## Checklist

**Every RDF file:**

- [X] Has at least one owl:sameAs property that links to another dataset

## Comments on the self-assessment
As merged-files.csv is the source for triplesmaps creating  addresses, districts and subdistricts class instances (the ones that can be directly linked with wikidata instances for concrete addresses, subdistricts and subdistricts),  reconciliation operations have been performed only on this file. The rest of the triplemaps don't make use of this "geographical" links. Analogously, econciliation for linking organizations names with wikidata entities have been performed only in the four datasets that are sources of triplesmaps for associations, federations, foundations and federations.

All properties with links pointing to an external knowledge graph are of type owl:sameAs except the one pointing to streets/sqares resources in wikidata. The reasson of this is that our address class refers not to the street/sqare itself where our entity is based on, but to the concrete location (building and location inside the building). Thus, both entities are not the same (we could say that instances of class address are contained inside the pointing wikidata entities).

Aplying SHACL shapes to our knowledge graph, we discovered three type declaration errors in our ontology that have remained unnoticed. The type declarations for latitude, longitude and zipcode were incorrrectly setted in the ontology statement (float instead of double for the first two and integer instead of string for the last). A new file ("ontology-fixed-after-shacl.ttl") with the fixed ontology was added in ./ontology/ directory. Shapes for the old and the fixed ontology have been also added, as well as the validation reports for both cases.