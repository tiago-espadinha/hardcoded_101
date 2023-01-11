import click
from rich.console import Console

console = Console()

from .scaffold.command import scaffold

@click.group()
def main():
    """DevKit: A collection of polished CLI tools."""
    pass

main.add_command(scaffold)

if __name__ == "__main__":
    main()