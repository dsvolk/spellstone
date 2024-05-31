import os
from dotenv import load_dotenv
load_dotenv(override=True)

from langchain.chains import GraphCypherQAChain
from langchain_community.graphs import Neo4jGraph
from langchain_openai import ChatOpenAI


NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get('NEO4J_USERNAME')
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')
NEO4J_DATABASE = os.environ.get('NEO4J_DATABASE')
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def test_connection():
    kb = Neo4jGraph(url=NEO4J_URI, username=NEO4J_USERNAME, password=NEO4J_PASSWORD, database=NEO4J_DATABASE)
    # chain = GraphCypherQAChain(kb)

    return kb.query('MATCH (n) RETURN n LIMIT 1')