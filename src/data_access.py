import os
import json
from xmlrpc.client import Boolean
from expense import Expense

DATA_FILE = "data/expenses.json"

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