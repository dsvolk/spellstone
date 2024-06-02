# Spellstone
Spellstone is a system of services and tools to augment your Obsidian knowledge base with automations and powerful AI tools

## Installation

### Set up API keys for the bot
The bot requires some API keys to run. There are two ways of providing them:
- environment variables. Provide the env variables listed in `template.env`. This option is more convenient for a cloud installation.
- `.env` file in the project root. You should manually create it. I do not provide my own `.env` file because of security reasons, but I put `template.env` as a template for the keys required. This option is better suited for a local installation.

#### Get OpenAI API key
Set up your own OpenAI account. Visit [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys) in your OpenAI account to create a new API key.

#### Get Cohere API key
...and the same for Cohere. Visit [https://dashboard.cohere.ai/](https://dashboard.cohere.ai/) to create a new API key.

### Cloud installation
For most clouds, it should be sufficient to just push the git repo and let them build everything for you. This, for example, works for [Railway](https://railway.app/), [Heroku](https://www.heroku.com/), and others. The repo already has the Dockerfile and Makefile provided.

So all you need is to set up the API keys as described above.

### Local installation
#### VAULT_DIR
Make `VAULT_DIR` in `.env` point at your Obsidian vault. This is the folder where your Obsidian vault is located. The bot will read and write to this folder.

#### Set up Poetry (Python package manager)
```console
curl -sSL https://install.python-poetry.org | python3 -
poetry --version
poetry config virtualenvs.in-project true
```

#### Set up Python environment
(in the project folder)
```console
poetry install --with=bot,dev,test,dashboard,etl,tools --no-root
poetry run pre-commit install
```
OR
```console
make install
```

#### Start Neo4j database
```console
make neo4j
```

#### Run the Backend service
(in the project folder)
```console
poetry run python -m src.app
```
OR
```console
make run
```

Use Ctrl+c to stop the Backend.

## Development
### Debugging in VSCode
When debugging, select "Python: Module" configuration.

## Enjoy!
