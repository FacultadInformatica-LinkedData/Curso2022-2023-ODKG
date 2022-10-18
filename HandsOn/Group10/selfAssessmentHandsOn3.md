# Hands-on assignment 3 – Self assessment

## Checklist

**Every resource described in the CSV file:**

- [X] Has a unique identifier in a column (not an auto-increased integer)
- [X] Is related to a class in the ontology

**Every class in the ontology:**

- [X] Is related to a resource described in the CSV file

**Every column in the CSV file:**

- [X] Is trimmed
- [X] Is properly encoded (e.g., dates, booleans)
- [X] Is related to a property in the ontology

**Every property in the ontology:**

- [X] Is related to a column in the CSV file

## Comments on the self-assessment
We decided to create a single csv for each class of our ontology because we thoght it would make easier the later mapping.

To create Districts, neighbourhoods, streets and locations csv files we used python rather tan OpenRefine.

We also decided to change the object of the blockId property to a string rather tan an integer, so we changed that in the ontology file.

Finally we compressed the parking meter tickets csv file because due to the changes in the file it exceeded the 100 MB max size of github
