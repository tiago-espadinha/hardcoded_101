import click
from rich.console import Console

console = Console()

@click.group()
def finance():
    """Track personal finances."""
    pass

@finance.command()
@click.argument("amount", type=float)
@click.argument("category")
@click.option("--description", help="Description of transaction")
@click.option("--date", help="Date of transaction (YYYY-MM-DD)")
def add(amount, category, description, date):
    """Add a transaction."""
    console.print(f"[bold green]Adding transaction: {amount} in {category}...[/bold green]")

@finance.command()
@click.option("--month", help="Filter by month (YYYY-MM)")
@click.option("--category", help="Filter by category")
@click.option("--limit", type=int, default=10, help="Number of items to show")
def list(month, category, limit):
    """List transactions."""
    console.print("[bold cyan]Listing transactions...[/bold cyan]")

@finance.command()
@click.option("--month", help="Summary for specific month (YYYY-MM)")
def summary(month):
    """Show financial summary."""
    console.print("[bold yellow]Generating financial summary...[/bold yellow]")

@finance.command()
@click.option("--format", type=click.Choice(["json", "csv"]), default="json", help="Export format")
@click.option("--output", "-o", help="Output file")
def export(format, output):
    """Export transactions."""
    console.print(f"[bold blue]Exporting transactions to {format}...[/bold blue]")