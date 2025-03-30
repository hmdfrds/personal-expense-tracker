from email.policy import default
import click
from expense import Expense
from data_access import *
from rich.console import Console
from rich.table import Table

from reports import report_by_category, report_by_month

console = Console()

@click.group()
def cli():
    pass

@cli.command()
@click.option("--date", prompt="Date (DD-MM-YYYY)", help="Date of the expense")
@click.option("--amount", type= float, prompt="Amount", help="Amount spent")
@click.option("--category", prompt="Category", help="Category of expense")
@click.option("--description", prompt="Description", help="Short description of expense")
def add(date, amount, category, description):
    expense = Expense(date=date, amount=amount,category=category, description=description)
    add_expense(expense)
    console.print("[green]Expense added successfully![/green]")

@cli.command()
def list():
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]No expenses recorded yet.[/yellow]")
        return
    table = Table(title="Expense Records")
    table.add_column("ID", style="cyan", overflow='ignore')
    table.add_column("Date", style="magenta")
    table.add_column("Amount", style="green")
    table.add_column("Category", style="blue")
    table.add_column("Description", style="white")

    for exp in expenses:
        table.add_row(exp.id[:8], exp.date, f"${exp.amount:.2f}", exp.category, exp.description)
    console.print(table)

@cli.command()
@click.option("--id", prompt="Expense ID", help="ID of the expense to edit")
@click.option("--date", default= None, help="New date (DD-MM-YYYY)")
@click.option("--amount", type=float, default=None, help="New amount")
@click.option("--category", default=None, help="New category")
@click.option("--description", default=None, help="New description")
def edit(id, date,amount, category, description):
    new_data = {k:v for k,v in {"date": date, "amount": amount, "category": category, "description": description}.items() if v is not None}
    if update_expense(id, new_data):
        console.print(f"[green]Expense {id} updated![/green]")
    else:
        console.print("[yellow]Expense ID not found![/yellow]")

@cli.command
@click.option("--type", type=click.Choice(["month", "category"], case_sensitive=False), prompt="Report type (month/category)")
def report(type):
    if type == "month":
        report_by_month()
    elif type == "category":
        report_by_category()

if __name__ == "__main__":
    cli()