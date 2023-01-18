import click
from rich.console import Console

console = Console()

from .scaffold.command import scaffold
from .vault.command import vault

@click.group()
def main():
    """DevKit: A collection of polished CLI tools."""
    pass

main.add_command(scaffold)
main.add_command(vault)

if __name__ == "__main__":
    main()