@prefix : <http://Assignment2b.org/node#>.
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix rel: <http://Assignment2b.org/rel#>.

:Class01
    rel:inclues :Sensor029;
    rel:inclues :Computer101.

:Sensor029  
    rel:hasMeasurement :Measurement8401.

:Computer101
    rel:hasOwner :User10A.

:User10A
    rel:hasName "Pedro".

:Measurement8401  
    rel:atTime "2010-06-12T12:00:12"^^xsd:dateTime;
    rel:hasTemperature 29.