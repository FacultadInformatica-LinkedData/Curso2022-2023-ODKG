import folium, numpy
from datetime import datetime

POP_MIN_WIDTH="400"
POP_MAX_WIDTH="400"
IMG_WIDTH="150"
IMG_HEIGHT="200"

def builder(item: dict) -> folium.Popup:

  db = ""
  if 'db' in item:
    try:
      fecha = datetime.strptime(item["db"]["value"], '%Y-%m-%dT%H:%M:%SZ')
      db = f"""<strong>Date of birth: </strong>{fecha.strftime('%Y-%m-%d')}<br />"""
    except (ValueError, TypeError):
      db = ""

  dd = ""
  if 'dd' in item:
    try:
      fecha = datetime.strptime(item["dd"]["value"], '%Y-%m-%dT%H:%M:%SZ')
      dd = f"""<strong>Date of death: </strong>{fecha.strftime('%Y-%m-%d')}<br />"""
    except (ValueError, TypeError):
      db = ""

  pb = ""
  if 'pb' in item:
      pb = f"""<strong>Place of birth: </strong>{item["pb"]["value"]}<br />"""

  occupation = ""
  if 'occupation_list' in item:
      occupation = f"""<strong>Occupation: </strong>{item["occupation_list"]["value"]}<br />"""

  bne = ""
  if 'bne' in item:
    bne = f"""<h4><a href=\"http://datos.bne.es/resource/{item["bne"]["value"]}" target=\"_blank\">More Info in BNE</a></h4>"""

  imagen = f"""<img src=\"https://clipground.com/images/available-clipart-4.jpg\" width=\"{IMG_WIDTH}px\" height=\"{IMG_HEIGHT}px\" alt=\"Not available\">"""
  if 'imgw' in item:
    imagen = f"""<img src=\"{item["imgw"]["value"]}\" width=\"{IMG_WIDTH}px\" height=\"{IMG_HEIGHT}px\" alt=\"{item["nombre"]["value"]}\">"""

  body = f"""
  <div>
  <center>
   <div style="float:left;vertical-align: middle;max-width: 50%;">
    <a href={item["entidad_wikidata"]["value"]} target="_blank"><h3>{item["nombre"]["value"]}</h3></a>
    {db}
    {dd}
    {pb}
    {occupation}
    {bne}
   </div>
   <div style="/* float: none; */overflow: hidden;display: block;max-width: 50%;">
    {imagen}
   </div>
   <div style="clear: both;"></div>
  </center>
  <hr/>
  <div style="overflow: hidden;"> 
   <p> 
    <strong>Date: </strong>{item["fecha"]["value"]}<br />
    <strong>Address: </strong>{item["direccion"]["value"]}<br />
    <strong>District: </strong><a href="{item["distrito_wikidata"]["value"]}" target="_blank">{item["distrito_nombre"]["value"]}</a><br />
    <strong>Keywords: </strong>{item["keywords"]["value"]}<br />
   </p>
   </div>
  <hr/>
  <div>
    <h4><string>Description</strong></h4>
    <p style="overflow: hidden; text-overflow: ellipsis;">{item["descripcion"]["value"]}</p>
    <p>
      <a href="{item["web_url"]["value"]}" target="_blank">More info.</a>
    </p>
  </div>
  </div>
  """
  return folium.Popup(folium.IFrame(body), min_width=POP_MIN_WIDTH, max_width=POP_MAX_WIDTH)
