import os

HELIO_SERVER = os.environ.get("HELIO_SERVER", "http://localhost:9000/sparql")
APP_HOST = os.environ.get("APP_HOST", "http://localhost")
APP_PORT = int(os.environ.get("APP_PORT", "8080"))