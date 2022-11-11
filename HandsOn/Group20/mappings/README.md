
The current versions for the ontology and the mappings, as well as for the knowledge graphs, the sparql queries and the shacl analysis can be accesed in their correspondent folders. Older versions for all of these files (the ones corresponding with what we had prior to HOEvaluation1) have been stored in "previous-files" folders, created for that purpose.

"mapping-rules-until-assignment-5.yml",  "template-rml.ttl" and "template-rml-with-links-until-assigment-5" correspond with what we had to deliver for the 5th and previous assignments (the mappings before reusing other existing ontologies in our case) once we have taken into account H0Evaluation1's comments and fixed things according to that. "mapping-rules.yml" and "template-rml-with-links.ttl" corresponds to the results for the final assignment.

After HOEvaluation1, several changes have been performed both in the ontology and the mappings, in order to improve our knowledge graph based on the recommendations made. 

    - Datatype properties checked: some ranges have been changed.
    - Naming strategy reviewed: subClass path deleted.
    - Some triplesmaps URI's modified: avoidance of redundancies and more meaningful identifiers.
    - Date format fixed. Float changed to double. 
    - Email and phone classes transformed in datatype properties of CollaborativeEntities subclasses. Website class has been left unchanged, thus reflecting the fact that website uses to be a separate class in other ontologies.
    - URI`s now coded as such.
    - website_uri codified as an actual URI (represented before as a string)
    - additional inconsistency between ontology and mappings fixed: the property asoc_affiliated previously named "asoc_madrid" in the mappings.


