from langchain_community.graphs import Neo4jGraph

from .config import Neo4jConfig

# OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')


def test_connection():
    kb = Neo4jGraph(
        url=Neo4jConfig.NEO4J_URI,
        username=Neo4jConfig.NEO4J_USERNAME,
        password=Neo4jConfig.NEO4J_PASSWORD,
        database=Neo4jConfig.NEO4J_DATABASE,
    )
    # chain = GraphCypherQAChain(kb)

    return kb.query("MATCH (n) RETURN n LIMIT 1")
