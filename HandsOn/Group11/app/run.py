from utils import marker_builder as mb
from utils import sparql

from settings import *
from flask import Flask, render_template
from pathlib import Path

import folium

CWD = Path(__file__).parents[1].resolve().as_posix()

START_COORDS = [40.428285284058816, -3.7070024693800345]
START_ZOOM = 13
MAP_TYPE = "openstreetmap"
DISTRICT_COLORS = {
    "Chamartín": "green",
    "Arganzuela" : "blue",
    "Moncloa-Aravaca" : "pink",
    "Centro" : "black",
    "Salamanca" : "purple",
    "Tetuán" : "gray",
    "Moratalaz" : "lightgreen",
    "Latina" : "orange",
    "Chamberí" : "beige",
    "Puente_de_Vallecas" : "lightgray",
    "Carabanchel" : "cadetblue",
    "Retiro" : "red",
}

app = Flask(__name__)

map = folium.Map(
    location=START_COORDS, 
    tiles=MAP_TYPE, 
    zoom_start=START_ZOOM
)

@app.route('/')
def index() -> str:

    plaques_list = sparql.select_all()
    for item in plaques_list:
        folium.Marker(
            location=(
                item["lat"]["value"], 
                item["lon"]["value"]),
            icon=folium.Icon(
                color=DISTRICT_COLORS.get(item["distrito_nombre"]["value"], ""),
                icon='map-marker'),
            popup=mb.builder(item)
        ).add_to(map)

    map.save(CWD + '/app/templates/map.html')
    # rendeR_template uses the HTML files inside 'templated' directory
    return render_template('map.html')


@app.route('/templates/map')
def reload_map() -> str:
    return render_template('map.html')


if __name__ == '__main__':
#    app.run(debug=True, host=APP_HOST, port=APP_PORT)
    app.run(debug=True, host="127.0.0.1", port=8080)