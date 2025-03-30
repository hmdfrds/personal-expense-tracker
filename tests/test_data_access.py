import os
import json
from data_access import add_expense, delete_expense, load_expenses, delete_expense, save_expenses, update_expense, get_expense_by_id
from expense import Expense

TEST_FILE = "data/test_expenses.json"

def setup_module(module):
    global TEST_FILE
    module.original_data_file = "data/expenses.json"
    os.remove(TEST_FILE) if os.path.exists(TEST_FILE) else None
    os.rename(module.original_data_file, TEST_FILE) if os.path.exists(module.original_data_file) else None

def teardown_module(module):
    global TEST_FILE
    os.remove(module.original_data_file) if os.path.exists(module.original_data_file) else None
    os.rename(TEST_FILE, module.original_data_file) if os.path.exists(TEST_FILE) else None

def test_add_expense():
    expense = Expense(date="30-03-2025", amount=50.0, category="Transport", description="Bus ticket")
    add_expense(expense)
    retrieved = get_expense_by_id(expense.id)
    assert retrieved is not None
    assert retrieved.id == expense.id

def test_update_expense():
    expense = Expense(date="30-03-2025", amount=10.0, category="Food", description="Coffee") 
    add_expense(expense)
    update_expense(expense.id, {"amount": 25.0}) 
    updated_expense = get_expense_by_id(expense.id)
    assert updated_expense.amount == 25.0

def test_delete_expense():
    expense = Expense(date="30-03-2025", amount=15.0, category="Entertainment", description="Movie ticket")
    add_expense(expense)
    delete_expense(expense.id)
    assert get_expense_by_id(expense.id) == None