import os

import click
from dotenv import load_dotenv

from .mdparse import parse_note
from .neo4j import test_connection

# Load environment variables from .env file
load_dotenv(override=True)


@click.group()
def cli():
    pass


def scan_directory(directory):
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d not in [".trash", ".obsidian"]]
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files


@cli.command()
@click.option(
    "--directory",
    default=lambda: os.getenv("OBSIDIAN_VAULT_DIR", "."),
    help="Directory to scan for Markdown files",
)
def scan(directory):
    """Output a list of Markdown files in a directory."""
    try:
        markdown_files = scan_directory(directory)

        for file in markdown_files:
            click.echo(file)
    except FileNotFoundError:
        click.echo(f"Directory '{directory}' not found.")


@cli.command()
@click.option(
    "--file",
    default=lambda: os.getenv("OBSIDIAN_DEFAULT_FILE", "."),
    help="Markdown file to parse",
)
def parse(file):
    """Parse a particular Markdown file and output all its frontmatter values and sections."""
    try:
        metadata, content, sections = parse_note(file)
        click.echo("Metadata:")
        for key, value in metadata.items():
            click.echo(f"{key}: {value}")
        click.echo("\nSections:")
        for section in sections:
            click.echo(section.title)
    except FileNotFoundError:
        click.echo(f"File '{file}' not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


@cli.command()
def test():
    """Test the Obsidian vault is there"""
    try:
        n_files = len(scan_directory(os.getenv("OBSIDIAN_VAULT_DIR")))
        click.echo(f"✅ Found {n_files} Markdown files.")
    except FileNotFoundError:
        click.echo(f"❌ Directory '{os.getenv('OBSIDIAN_VAULT_DIR')}' not found.")

    """Test Neo4j connection"""
    try:
        n_nodes = len(test_connection())
        click.echo(f"✅ Found {n_nodes} nodes in the graph.")
    except Exception as e:
        click.echo(f"❌ Error connecting to Neo4j: {e}")


@cli.command()
def index():
    """Index all Markdown files in the Obsidian vault."""
    try:
        markdown_files = scan_directory(os.getenv("OBSIDIAN_VAULT_DIR"))

        for file in markdown_files:
            metadata, content, sections = parse_note(file)
            click.echo(f"Indexing {file}...")
            click.echo(f"Metadata: {metadata}")
            click.echo(f"Content: {content}")
            click.echo(f"Sections: {sections}")
    except FileNotFoundError:
        click.echo(f"Directory '{os.getenv('OBSIDIAN_VAULT_DIR')}' not found.")
    except Exception as e:
        click.echo(f"An error occurred: {e}")


if __name__ == "__main__":
    cli()
