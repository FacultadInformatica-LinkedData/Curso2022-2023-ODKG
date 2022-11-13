from flask import Flask, render_template, request
import requests
import urllib

# Creación de la aplicación
app = Flask(__name__)

def create_queries(health_area, province, city):
    if health_area == 'None' and province == 'None' and city == 'None':
        query = """PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#>
            PREFIX gn: <http://www.geonames.org/ontology#>
            PREFIX ns: <http://www.dialysisComunidadValenciana.es/>
            PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
            PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
            select distinct ?center_label ?phone ?address ?health_area_label ?city_label ?province_label ?entity_label where {
                ?center a ns:Center.
                ?center rdfs:label ?center_label.
                ?center ns:hasPhone ?phone. 
                ?center ns:hasAddress ?address.
                ?center ns:managed_by ?entity.
                ?entity a ns:Entity. 
                ?entity rdfs:label ?entity_label.
                ?center gn:locatedIn ?health_area.
                ?health_area a ns:Health_Area.
                ?health_area rdfs:label ?health_area_label.
                ?health_area gn:locatedIn ?city. 
                ?city a ns:City.
                ?city rdfs:label ?city_label.
                ?city gn:locatedIn ?province.
                ?province a ns:Province.
                ?province rdfs:label ?province_label
            } order by ?center_label"""

        response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query)}")

        tripletas = []
        for tripleta in response.json()["results"]["bindings"]:
            tripletas.append([tripleta["center_label"]["value"], tripleta["phone"]["value"], 
                tripleta["address"]["value"], tripleta["health_area_label"]["value"], tripleta["city_label"]["value"],
                tripleta["province_label"]["value"], tripleta["entity_label"]["value"]])
    
    else: 
        query = """
                    PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
                    PREFIX gn: <http://www.geonames.org/ontology#> 
                    PREFIX ns: <http://www.dialysisComunidadValenciana.es/> 
                    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
                    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 

                    select distinct ?center_label ?phone ?address ?entity_label where {
                    ?center a ns:Center. 
                    ?center ns:managed_by ?entity.
                    ?entity a ns:Entity.
                    ?entity rdfs:label ?entity_label.

                    ?center gn:locatedIn ?health_area.
                    ?health_area a ns:Health_Area."""
        
        if health_area != 'None':
            query = query + """?health_area rdfs:label\"""" + health_area + """\"^^xsd:string."""

        query +=  """?health_area gn:locatedIn ?city.
                    ?city a ns:City."""
        if city != 'None':
            query += """?city rdfs:label \""""+ city + """\"^^xsd:string ."""

        if province != "None":
            query += """?city gn:locatedIn ?province.
            ?province a ns:Province.
            ?province rdfs:label \""""+ province + """\"^^xsd:string."""
        
        query += """?center rdfs:label ?center_label.
            ?center ns:hasPhone ?phone.
            ?center ns:hasAddress ?address.
            }
            order by ?center_label"""
        
        response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query)}")

        tripletas = []
        for tripleta in response.json()["results"]["bindings"]:
            tripletas.append([tripleta["center_label"]["value"], tripleta["phone"]["value"], 
                tripleta["address"]["value"], tripleta["entity_label"]["value"]])

    return tripletas

# Main site
@app.route('/')
def index():
    query = """ PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
                PREFIX gn: <http://www.geonames.org/ontology#> 
                PREFIX ns: <http://www.dialysisComunidadValenciana.es/> 
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
                select distinct ?health_area where {
                    ?area a ns:Health_Area.
                    ?area rdfs:label ?health_area.
                }
                order by ?area
                """
    response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query)}")
    areas = []
    for tripleta in response.json()["results"]["bindings"]:
        areas.append(tripleta["health_area"]["value"])
    

    query = """ PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
                PREFIX gn: <http://www.geonames.org/ontology#> 
                PREFIX ns: <http://www.dialysisComunidadValenciana.es/> 
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
                select distinct ?province where {
                    ?x a ns:Province.
                    ?x rdfs:label ?province.
                }
                order by ?label
                """
    response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query)}")
    provinces = []
    for tripleta in response.json()["results"]["bindings"]:
        provinces.append(tripleta["province"]["value"])


    query = """ PREFIX geo: <http://www.w3.org/2003/01/geo/wgs84_pos#> 
                PREFIX gn: <http://www.geonames.org/ontology#> 
                PREFIX ns: <http://www.dialysisComunidadValenciana.es/> 
                PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> 
                PREFIX xsd: <http://www.w3.org/2001/XMLSchema#> 
                select distinct ?city where {
                    ?x a ns:City.
                    ?x rdfs:label ?city.
                }
                order by ?label
                """
    response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query)}")
    cities = []
    for tripleta in response.json()["results"]["bindings"]:
        cities.append(tripleta["city"]["value"])

    return render_template("home.html", health_areas=areas, provinces=provinces, cities=cities)


@app.route('/get_values', methods=['post'])
def get_values():
    health_area = request.form.getlist('health_area')
    province = request.form.getlist('province')
    city = request.form.getlist('city')
    queries = create_queries(health_area[0], province[0], city[0])

    return render_template("results.html", health_area=health_area, province=province, city=city, queries=queries)

# Init the app
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)

