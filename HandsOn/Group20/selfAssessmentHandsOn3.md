# Hands-on assignment 3 – Self assessment

## Checklist

**Every resource described in the CSV file:**

- [x] Has a unique identifier in a column (not an auto-increased integer)
- [x] Is related to a class in the ontology

**Every class in the ontology:**

- [x] Is related to a resource described in the CSV file

**Every column in the CSV file:**

- [x] Is trimmed
- [x] Is properly encoded (e.g., dates, booleans)
- [x] Is related to a property in the ontology

**Every property in the ontology:**

- [x] Is related to a column in the CSV file

## Comments on the self-assessment

As the fourth .csv files we are working with refers to different subclasses  of a main subclass (CollaborativeEntities) and their structures are almost the same, we have performed an homogeneization task in order to merge them and get a single .csv file, called merged_entities.csv. This new .csv file includes a label who identifies to which subclass of CollaborativeEntities instances below. In next assignments, we will try to take advantage to this new dataset, using instead the separated cleanised datasets if we find more comfortable to transform data to RDF standards at this way. 

Using the google API services, we've achieved to obtain precise geographical information about latitudes and longitudes related to each adress we have. To reach that aim, we had to create a google cloud platform facturation account. With the $300 of free credit we have been able to request that data without problem.  We have used the following GREL expression.

'https://maps.googleapis.com/maps/api/geocode/json?' + 
'sensor=false&' + 
'key=[key_value]' +
'address=' + escape(value,'url')


As identifiers for entities defined in Madrid City Council datasets were auto-incremental integers, we have applied a hash md5 function to them, in order to prevent it. 

In Asociaciones_202209.csv, some duplicated IDs where present. This dataset includes information about to which federations an association belongs to. As an association can belong to several federations, there are as many rows per record as federations an association belongs to for instances fitting with this fact. To prevent that and ensure that IDs are unique, data regarding to this has been transformed, so that information related with this kind of relationships is now represented as a list of JSON documents, where each federation the association belongs to is listed in one of them. 