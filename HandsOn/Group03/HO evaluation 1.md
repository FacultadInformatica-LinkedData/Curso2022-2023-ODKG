3
    Analysis
    Ontology
        - Some of the properties defined with numbers as ranges are not numbers.
        - Fix "haslocalization" -> "hasLocalization".
        - Coordinates are numbers.
    RDF data
        - Remove empty values: "NaN", "-".
        - Solve the character encoding issues.
        - URIs are encoded as strings.
        - Trim strings before adding them to the RDF.
        - Some string values include information that is not correct.
        - Some values could be represented as booleans (even if you don't include all the information from the file).
