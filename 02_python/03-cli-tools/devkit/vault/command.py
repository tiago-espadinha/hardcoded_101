import click
from rich.console import Console

console = Console()

@click.group()
def vault():
    """Securely manage passwords."""
    pass

@vault.command()
@click.argument("service")
@click.option("--username", help="Username for the service")
@click.option("--generate", type=int, help="Generate a random N-character password")
def add(service, username, generate):
    """Add an entry."""
    console.print(f"[bold green]Adding entry for {service}...[/bold green]")

@vault.command()
@click.argument("service")
@click.option("--show", is_flag=True, help="Reveal the password")
def get(service, show):
    """Get an entry."""
    console.print(f"[bold blue]Getting entry for {service}...[/bold blue]")

@vault.command()
@click.option("--search", help="Search for a service")
def list(search):
    """List all services."""
    console.print("[bold cyan]Listing all entries...[/bold cyan]")

@vault.command()
@click.argument("service")
def delete(service):
    """Delete an entry."""
    if click.confirm(f"Are you sure you want to delete {service}?"):
        console.print(f"[bold red]Deleting entry for {service}...[/bold red]")

@vault.command()
@click.option("--format", type=click.Choice(["json", "csv"]), default="json", help="Export format")
@click.option("--output", "-o", help="Output file")
def export(format, output):
    """Export all entries."""
    console.print(f"[bold yellow]Exporting all entries to {format}...[/bold yellow]")