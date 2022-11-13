from flask import Flask, render_template, request
import requests
import urllib

# Creación de la aplicación
app = Flask(__name__)

def create_queries(health_area, province, city):
    query1 = """
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
        query1 = query1 + """?health_area rdfs:label\"""" + health_area + """\"^^xsd:string."""

    query1 +=  """?health_area gn:locatedIn ?city.
                 ?city a ns:City."""
    if city != 'None':
        query1 += """?city rdfs:label \""""+ city + """\"^^xsd:string ."""

    if province != "None":
        query1 += """?city gn:locatedIn ?province.
        ?province a ns:Province.
        ?province rdfs:label \""""+ province + """\"^^xsd:string."""
    
    query1 += """?center rdfs:label ?center_label.
        ?center ns:hasPhone ?phone.
        ?center ns:hasAddress ?address.
        }
        order by ?center_label"""
    
    response = requests.get(f"http://localhost:8080/sparql?query={urllib.parse.quote_plus(query1)}")

    tripletas = []
    for tripleta in response.json()["results"]["bindings"][0:10]:
        tripletas.append([tripleta["center_label"]["value"], tripleta["phone"]["value"], 
            tripleta["address"]["value"], tripleta["entity_label"]["value"]])


    return [tripletas, response.json()["results"]["bindings"][0:10]]

# Main site
@app.route('/')
def index():
    # select distinct ?health_area where {
    #     ?area a ns:Health_Area.
    #     ?area rdfs:label ?health_area.
    # }
    # order by ?area
    areas = ['Alicante', 'Dpto. Salud Alcoi', 'Dpto. Salud Alicante', 'Dpto. Salud Denia', 'Dpto. Salud Elche',
    'Dpto. Salud Elche - Crevillente', 'Dpto. Salud Elda', 'Dpto. Salud Elda', 'Dpto. Salud Marina Baixa',
    'Dpto. Salud Orihuela', 'Dpto. Salud San Juan', 'Dpto. Salud Torrevieja', 'H. Arnau-Lliria']
    provinces = ['Alicante Province', 'Castellón', 'Valencia Province']
    cities = ['Alfafar', 'Alicante', 'Benidorm', 'Burjassot', 'Castelló de la Plana', 'Catarroja', 'Dénia', 'Elche', 'Elda',
    'Gandia', 'La Vall d\'Uixó', 'Llíria', 'Masamagrell', 'Orihuela', 'Oropesa del Mar', 'Paterna', 'Port de Sagunt', 'Requena',
    'San Vicente del Raspeig', 'Torrent', 'Torrevieja', 'Valencia', 'Vila-real', 'La Vila Joiosa', 'Vinaròs', 'Xirivella']
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

