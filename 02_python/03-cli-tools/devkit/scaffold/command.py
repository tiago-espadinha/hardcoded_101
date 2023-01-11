import click
from rich.console import Console

console = Console()

@click.command()
@click.argument("template")
@click.argument("project_name")
@click.option("--output", "-o", help="Output directory")
@click.option("--git", is_flag=True, help="Initialise a git repo")
@click.option("--venv", is_flag=True, help="Create and activate a virtual environment")
def scaffold(template, project_name, output, git, venv):
    """Scaffold a new project from a template."""
    console.print(f"[bold green]Scaffolding {template} project: {project_name}...[/bold green]")
    # Implementation placeholder
    pass