from flask import Flask, render_template, url_for, request
from rdflib import Graph, Literal
from rdflib.plugins import sparql

app = Flask(__name__)
graph = Graph()
graph.parse("output-ntriples-with-links.nt", format="nt")


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/search/", methods=["GET"])
def search():
    return executeQuery(
        request.args.get("district"),
        request.args.get("subdistrict"),
        request.args.get("purpose"),
        request.args.get("organization"),
    )


def executeQuery(district, subdistrict, purpose, organization):
    bindings = {}
    if district:
        bindings["d"] = Literal(district)
    if subdistrict:
        bindings["sd"] = Literal(subdistrict)
    if purpose:
        bindings["p"] = Literal(purpose)

    orgs = (
        [organization]
        if organization
        else ["Association", "Collective", "Federation", "Foundation"]
    )
    allQueryResults = {}

    for org in orgs:
        queryResult = graph.query(buildQuery(org), initBindings=bindings)
        results = []

        for row in queryResult:
            results.append(
                {
                    "name": str(row.name),
                    "latitude": float(row.latitude),
                    "longitude": float(row.longitude),
                    "num_affiliates": int(row.num_affiliates),
                    "telephone": str(row.telephone),
                    "email": str(row.email),
                    "uri": str(row.uri),
                    "founding_date": str(row.founding_date)
                }
            )

        allQueryResults[org] = results

    return allQueryResults


def buildQuery(organization):
    stringQuery = """
    prefix schema: <https://schema.org/>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix class: <https://www.asociadrid.es/ontology/class#>
    prefix dasp:<http://vocab.linkeddata.es/datosabiertos/def/sector-publico/territorio#>
    prefix property: <https://www.asociadrid.es/ontology/property#>
    prefix org:<http://www.w3.org/ns/org#>
    SELECT ?name ?latitude ?longitude ?num_affiliates ?telephone ?email ?uri ?founding_date WHERE
    {
        ?elem rdf:type class:%s.
        ?elem schema:legalName ?name.
        ?elem org:purpose ?p.
        ?elem property:num_affiliates ?num_affiliates.
        ?elem schema:foundingDate ?founding_date.
        ?elem schema:location ?location.
        ?location schema:latitude ?latitude.
        ?location schema:longitude ?longitude.
        ?location dasp:barrio ?subdistrict.
        ?subdistrict property:subdistrict_label ?sd.
        ?subdistrict dasp:distrito ?district.
        ?district property:district_label ?d
        OPTIONAL {
            ?elem schema:telephone ?telephone.
            ?elem schema:email ?email.
            ?elem property:hasAWebsite ?website.
            ?website property:website_uri ?uri.
        }
    }
    """ % (
        organization
    )
    return sparql.prepareQuery(stringQuery)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
