7
    Analysis
        - If the license is of type "share-alike", you cannot change the license in your dataset.
    Ontology
        - The name of the property between Municipality and Station is strange (isLocatedIn). It should be the other way around.
        - xsd:real does not exist.
        - owl:SubClassOf is not correctly written.
        - Do not implement the ontology by hand, use some ontology editor. The tools already take car of some of the problems that you had.
    RDF data
        - All the magnitudes are mixed into a single one with all the values.
        - Trim strings before adding them to the RDF.
        - SAREF has properties for defining the units of measurement and the properties of the measurement.
