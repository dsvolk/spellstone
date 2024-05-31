neo4j:
	docker run \
		--name neo4j \
		-p 7474:7474 -p 7687:7687 \
		-d \
		-v $(PWD)/local/neo4j/data:/data \
		-v $(PWD)/local/neo4j/logs:/logs \
		-v $(PWD)/local/neo4j/import:/var/lib/neo4j/import \
		-v $(PWD)/local/neo4j/plugins:/plugins \
		-e NEO4J_AUTH=neo4j/password \
		-e NEO4J_PLUGINS=\[\"apoc\"\]  \
		neo4j:latest

env:
	poetry install --with dev,test --no-root

# install: env
# 	poetry run pre-commit install

test:
	poetry run python -m indexer.cli test
