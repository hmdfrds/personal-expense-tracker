import pytest
import os
from click.testing import CliRunner

from cli import cli

runner = CliRunner()
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
    result = runner.invoke(cli, ["add", "--date", "30-03-2025", "--amount", "15.00", "--category", "Food", "--description", "Dinner"])
    assert "Expense added" in result.output

def test_list_expenses():
    result = runner.invoke(cli, ["list"])
    assert "ID" in result.output
    assert "Category" in result.output
    