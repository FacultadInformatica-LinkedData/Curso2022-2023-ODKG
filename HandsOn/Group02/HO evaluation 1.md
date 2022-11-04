2
    Analysis
    Ontology
        - In OWL, there are object properties (where value of the property is a resource) and datatype properties (where the value of the property is a string literal, usually typed).  Right now you are only using object properties, which is wrong.
        - You are redefining XML schema datatypes as classes.
        - District names should not be XMLLiteral.
    RDF data
        - Some URIs en with a whitespace "%20".
        - The RDF file does not use the class and property URIs defined in the ontology.
