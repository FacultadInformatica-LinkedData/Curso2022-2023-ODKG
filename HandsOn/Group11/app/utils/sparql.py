from SPARQLWrapper import SPARQLWrapper, JSON
from settings import HELIO_SERVER

sparql = SPARQLWrapper(HELIO_SERVER)

SELECT_ALL = """
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX ns: <http://placasdemadrid.linkeddata.es/placas-madrid/ontology/>

SELECT DISTINCT ?nombre ?descripcion ?direccion ?fecha ?idioma ?keywords ?titular_derechos ?lat ?lon ?distritoID ?distrito_nombre ?distrito_wikidata ?entidad_wikidata ?web_url WHERE {

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
}
"""


def select_all() -> list:
  return exec_query(SELECT_ALL)["results"]["bindings"]


def exec_query(query: str) -> dict:
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()  # type: ignore
