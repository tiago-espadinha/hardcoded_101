import click
from rich.console import Console

console = Console()

@click.group()
def main():
    """DevKit: A collection of polished CLI tools."""
    pass

if __name__ == "__main__":
    main()