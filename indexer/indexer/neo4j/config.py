import os as os
from dotenv import load_dotenv

load_dotenv(override=True)


class Neo4jConfig:
    NEO4J_URI = os.environ.get('NEO4J_URI', None)
    NEO4J_USERNAME = os.environ.get('NEO4J_USERNAME', None)
    NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD', None)
    NEO4J_DATABASE = os.environ.get('NEO4J_DATABASE', None)