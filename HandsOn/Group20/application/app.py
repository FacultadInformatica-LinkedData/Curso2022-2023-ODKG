from flask import Flask, render_template, url_for, request
from rdflib import Graph
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
        request.args.get("category"),
        request.args.get("organization"),
    )


def executeQuery(district, subdistrict, category, organization):
    orgs = (
        [organization]
        if organization
        else ["Association", "Collective", "Federation", "Foundation"]
    )
    allQueryResults = {}

    for org in orgs:
        query = sparql.prepareQuery(buildQuery(org))
        queryResult = graph.query(query)
        results = []

        for row in queryResult:
            results.append(
                {
                    "name": str(row.name),
                    "latitude": float(row.latitude),
                    "longitude": float(row.longitude),
                }
            )

        allQueryResults[org] = results

    return allQueryResults


def buildQuery(className):
    return """prefix schema: <https://schema.org/>
    prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
    prefix class: <https://www.asociadrid.es/ontology/class#>
    SELECT ?name ?latitude ?longitude WHERE
    {
    ?elem rdf:type class:%s.
    ?elem schema:legalName ?name.
    ?elem schema:location ?location.
    ?location schema:latitude ?latitude.
    ?location schema:longitude ?longitude
    }""" % (
        className
    )


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=3000, debug=True)
