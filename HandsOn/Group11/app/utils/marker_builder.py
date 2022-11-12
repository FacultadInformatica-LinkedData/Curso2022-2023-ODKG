import folium


POP_MIN_WIDTH="400"
POP_MAX_WIDTH="400"


def builder(item: dict) -> folium.Popup:
  body = f"""
  <center>
    <a href={item["entidad_wikidata"]["value"]} target="_blank"><h3>{item["nombre"]["value"]}</h3></a>
  </center>
  <hr/>
  <p> 
    <strong>Date: </strong>{item["fecha"]["value"]}<br />
    <strong>Address: </strong>{item["direccion"]["value"]}<br />
    <strong>District: </strong><a href="{item["distrito_wikidata"]["value"]}" target="_blank">{item["distrito_nombre"]["value"]}</a><br />
    <strong>Keywords: </strong>{item["keywords"]["value"]}<br />
  </p>
  <hr/>
  <h4><string>Description</strong></h4>
  <p style="overflow: hidden; text-overflow: ellipsis;">{item["descripcion"]["value"]}</p>
  <p>
    <a href="{item["web_url"]["value"]}" target="_blank">More info.</a>
  </p>
  """
  return folium.Popup(folium.IFrame(body), min_width=POP_MIN_WIDTH, max_width=POP_MAX_WIDTH)
