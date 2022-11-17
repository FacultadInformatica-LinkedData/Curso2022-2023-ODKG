from SPARQLWrapper import SPARQLWrapper, JSON
import pandas as pd
from fastapi import Request, FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/fountains/{distno}")
async def fountains(distno: float):
  data= gettable(getdistfountains(distno))
  return Response(content=data, media_type="text/html")

@app.get("/nh/fountains/{nh}")
async def getnhfountains(nh):
    dist=getdistfromwd(nh)
    try:
        data= gettable(getdistfountains(dist))
    except:
        data= pd.DataFrame().to_html()
    return Response(content=data, media_type="text/html")

@app.get("/restrooms/{distno}")
async def restrooms(distno:float):
  data= gettable(getdistrestrooms(distno))
  return Response(content=data, media_type="text/html")

@app.get("/nh/restrooms/{nh}")
async def getnhrestrooms(nh):
    dist=getdistfromwd(nh)
    try:
        data= gettable(getdistrestrooms(dist))
    except:
        data= pd.DataFrame().to_html()
    return Response(content=data, media_type="text/html")

@app.get("/all/{distno}")
def all(distno:float):
    f=getdistfountains(distno)#fountains
    dff=pd.DataFrame(data=f)#dffountains
    dff=dff.assign(tipo="Fountain")
    r=getdistrestrooms(distno)#restrooms
    dfr=pd.DataFrame(data=r)#dfrestrooms
    dfr=dfr.assign(tipo="Restroom")
    dff=dff.append(dfr)
    dff.columns=["Address", "Type"]
    data= dff.to_html()
    return Response(content=data, media_type="text/html")

@app.get("/nh/all/{nh}")
def getnhall(nh):
    distno=getdistfromwd(nh)
    try:
      f=getdistfountains(distno)#fountains
      dff=pd.DataFrame(data=f)#dffountains
      dff=dff.assign(tipo="Fountain")
      r=getdistrestrooms(distno)#restrooms
      dfr=pd.DataFrame(data=r)#dfrestrooms
      dfr=dfr.assign(tipo="Restroom")
      dff=dff.append(dfr)
      dff.columns=["Address", "Type"]
      data= dff.to_html()
    except:
        data= pd.DataFrame().to_html()
    return Response(content=data, media_type="text/html")

def getdistfromnh(neighbourhood):

    sparql = SPARQLWrapper("https://query.wikidata.org/bigdata/namespace/wdq/sparql")
    sparql.setQuery("""
 SELECT DISTINCT ?d  WHERE {
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE]". }
  {
    SELECT DISTINCT ?d WHERE {
      ?item p:P31 ?statement0.
      ?statement0 (ps:P31/(wdt:P279*)) wd:Q10267336.
      ?item rdfs:label ?itemLabel. 
      FILTER(CONTAINS(LCASE(?itemLabel), "%s"@es)). 
      ?item p:P131 ?s.
      ?s (ps:P131/(wdt:P131*)) ?d.
      ?d p:P31 ?statement1.
      ?statement1 (ps:P31/(wdt:P279*)) wd:Q3032114.
    }
  }
}

    """%neighbourhood
    )
    a=[]
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    for result in results["results"]["bindings"]:
        a.append(str(result['d']['value']))

    return a

def getdistfromwd(nh):
    l=getdistfromnh(nh)
    if(len(l)!=1):
        return ""
    l=l[0].replace("entity", "wiki").replace("www.", "").replace("http", "https")
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery("""
    PREFIX p: <http://www.urbanElementsMadrid.es/ontology/ont#>
	PREFIX o: <http://www.w3.org/2002/07/owl#>
    SELECT distinct ?c ?w WHERE {
  
  	?c a p:District.
  	?c o:sameAs <%s>
}
      
      """%l 
    )
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    a=[]
    for result in results["results"]["bindings"]:
        a.append(str(result['c']['value']))
    
    try:
        return float(a[0].split("/")[-1])
    except:
        return ""

def getdistfountains(distno):
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery("""
    PREFIX p: <http://www.urbanElementsMadrid.es/ontology/ont#>
    SELECT distinct ?c WHERE {
      ?s a p:Fountain.
      ?s p:hasDistrict <http://www.urbanElementsMadrid.es/resource/District/"""+str(distno)+""">.
        ?s p:hasAddress ?f.
  		?f p:isLocated ?c
}
      
      """ 
    )
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    a=[]

    for result in results["results"]["bindings"]:

        a.append(str(result['c']['value']))

    return a


def getdistrestrooms(distno):
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery("""
    PREFIX p: <http://www.urbanElementsMadrid.es/ontology/ont#>
    SELECT distinct ?c WHERE {
      ?s a p:Restroom.
      ?s p:hasDistrict <http://www.urbanElementsMadrid.es/resource/District/"""+str(distno)+""">.
        ?s p:hasAddress ?f.
  		?f p:isLocated ?c
}
      
      """ 
    )
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    a=[]

    for result in results["results"]["bindings"]:

        a.append(str(result['c']['value']))

    return a


def getdistall(distno):
    sparql = SPARQLWrapper("http://localhost:8080/sparql")
    sparql.setQuery("""
    PREFIX p: <http://www.urbanElementsMadrid.es/ontology/ont#>
    SELECT distinct ?c WHERE {
      ?s p:hasDistrict <http://www.urbanElementsMadrid.es/resource/District/"""+str(distno)+""">.
        ?s p:hasAddress ?f.
  		?f p:isLocated ?c
}
      
      """ 
    )
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    a=[]

    for result in results["results"]["bindings"]:

        a.append(str(result['c']['value']))

    return a



def gettable(l):
    df=pd.DataFrame(data=l)
    df.columns=["Address"]
    return df.to_html()
        

