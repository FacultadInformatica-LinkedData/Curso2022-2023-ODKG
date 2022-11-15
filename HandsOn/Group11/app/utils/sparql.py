from SPARQLWrapper import SPARQLWrapper, JSON
from settings import HELIO_SERVER

sparql = SPARQLWrapper(HELIO_SERVER)

SELECT_ALL = """
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ns: <http://placasdemadrid.linkeddata.es/placas-madrid/ontology/>
PREFIX wdt: <http://www.wikidata.org/prop/direct/>


SELECT DISTINCT ?nombre ?descripcion ?direccion ?fecha ?idioma ?keywords ?titular_derechos ?lat ?lon ?distritoID ?distrito_nombre ?distrito_wikidata 
?entidad_wikidata ?web_url ?db ?dd ?pb ?bne ?imgw (GROUP_CONCAT(DISTINCT ?occupation; SEPARATOR = ", ") AS ?occupation_list)

WHERE {

  ?Placa ns:nombre ?nombre .
  ?Placa ns:descripcion ?descripcion .
  ?Placa ns:direccion ?direccion .
  ?Placa ns:fecha ?fecha .
  ?Placa ns:idioma ?idioma .
  ?Placa ns:palabraClave ?keywords .
  ?Placa ns:titularDerechos ?titular_derechos .

  ?Placa ns:tieneUbicacion ?Ubicacion.
  ?Ubicacion ns:latitud ?lat .
  ?Ubicacion ns:longitud ?lon .

  ?Placa ns:tieneDistrito ?Distrito .
  ?Distrito ns:nombre ?distrito_nombre .
  ?Distrito owl:sameAs ?distrito_wikidata .

  ?Placa ns:representa ?Entidad .
  ?Entidad owl:sameAs ?entidad_wikidata .

  ?Placa ns:tieneWeb ?Web .
  ?Web ns:url ?web_url .

  OPTIONAL{
   SERVICE <https://query.wikidata.org/sparql> {
     OPTIONAL{
        ?entidad_wikidata wdt:P569 ?db . # date of birth
       }
     OPTIONAL{
         ?entidad_wikidata wdt:P570 ?dd . # date of death
       }
     OPTIONAL{
         ?entidad_wikidata wdt:P19 ?pbe . # place of birth
         ?pbe rdfs:label ?pb . # nombre
         FILTER (LANG(?pb) = "en") .
       }
     OPTIONAL{
        ?entidad_wikidata wdt:P950 ?bne . # BNE id
       }
     OPTIONAL{
       ?entidad_wikidata wdt:P106 ?oc . # occupation category
       ?oc wdt:P373 ?occupation . # occupation label
      }
     OPTIONAL{
        ?entidad_wikidata wdt:P18 ?imgw . # image
       }
   }
  }

}

GROUP BY ?nombre ?descripcion ?direccion ?fecha ?idioma ?keywords ?titular_derechos ?lat ?lon ?distritoID ?distrito_nombre ?distrito_wikidata 
?entidad_wikidata ?web_url ?db ?dd ?pb ?bne ?imgw

# LIMIT 20
"""


def select_all() -> list:
  return exec_query(SELECT_ALL)["results"]["bindings"]


def exec_query(query: str) -> dict:
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()  # type: ignore
