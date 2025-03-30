from collections import defaultdict
from rich.console import Console
from rich.table import Table
from datetime import datetime
from data_access import load_expenses

console = Console()

def report_by_month():
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]No expenses recorded yet.[/yellow]")
        return

    monthly_totals = defaultdict(float)

    for exp in expenses:
        month = datetime.strptime(exp.date, "%d-%m-%Y").strftime("%m-%Y")
        monthly_totals[month] += exp.amount
    
    table = Table(title="Expense Report by Month")
    table.add_column("Month", style="magenta")
    table.add_column("Total Spending", style="green")

    for month , total in sorted(monthly_totals.items()):
        table.add_row(month, f"${total:.2f}")
    console.print(table)

def report_by_category():
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]No expenses recorded yet.[/yellow]")
        return

    category_totals = defaultdict(float)

    for exp in expenses:
        category_totals[exp.category] += exp.amount
    
    table = Table(title="Expense Report by Category")
    table.add_column("Category", style="blue")
    table.add_column("Total Spending", style="green")

    for category, total in sorted(category_totals.items()):
        table.add_row(category, f"${total:.2f}")

    console.print(table)