import os
import json
from xmlrpc.client import Boolean
from expense import Expense
from rich.console import Console

DATA_FILE = "data/expenses.json"
console = Console()
def load_expenses():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            data = json.load(file)
            return [Expense.from_dict(exp) for exp in data.get("expenses", [])]
    except (json.JSONDecodeError, FileNotFoundError):
        return [] 

def save_expenses(expenses: Expense):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump({"expenses": [exp.to_dict() for exp in expenses]}, file, indent=4)    

def add_expense(expense: Expense):
    expenses = load_expenses()
    expenses.append(expense)
    save_expenses(expenses)

def get_expense_by_id(id: str):
    expenses = load_expenses()

    for expense in expenses:
        if expense.id == id:
            return expense
    return None


def delete_expense(id: str):
    expenses = load_expenses()
    new_expenses = [expense for expense in expenses if expense.id != id]
    save_expenses(new_expenses)

def update_expense(id, new_data) -> Boolean:
    expenses = load_expenses()
    for expense in expenses:
        if expense.id == id:
            expense.date = new_data.get('date', expense.date)
            expense.amount = new_data.get('amount', expense.amount)
            expense.category = new_data.get('category', expense.category)
            expense.description = new_data.get('description', expense.description)
            save_expenses(expenses)
            return True
    return False

def export_data(file_path):
    expenses = load_expenses()
    if not expenses:
        console.print("[yellow]No expenses to export.[/yellow]")
        return
    data = {"expenses": [ exp.to_dict() for exp in expenses]}

    try:
        with open(file_path, "w") as f:
            json.dump(data, f, indent=4)
        console.print(f"[green]Exported data to {file_path}[/green]")
    except Exception as e:
        console.print(f"[red]Failed to export data: {e}[/red]")

def import_data(file_path):
    if not os.path.exists(file_path):
        console.print(f"[red]File not found: {file_path}[/red]")
        return
    with open(file_path, "r") as f:
        try:
            data = json.load(f)
            if "expenses" not in data or not isinstance(data["expenses"], list):
                raise ValueError("Invalid JSON format")
        except Exception as e:
            console.print(f"[red]Failed to import data: {e}[/red]")
            return
    confirm = input("This will overwrite existing data. Proceed? (y/n): ").strip()
    if confirm.casefold() != "y".casefold():
        console.print("[yellow]Import cancelled.[/yellow]")
        return

    expenses = [Expense(**exp) for exp in data["expenses"]]
    save_expenses(expenses)
    console.print(f"[green]Imported {len(expenses)} expenses from {file_path}[/green]")