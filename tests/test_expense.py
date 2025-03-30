import pytest
from expense import Expense
from datetime import datetime
import json


def test_expense_creation():
    expense = Expense(
        date="14-02-2025",
        amount=29.99,
        category="Food",
        description="Lunch",
    )
    assert expense.id is not None
    assert expense.date == "14-02-2025"
    assert expense.amount == 29.99
    assert expense.category == "Food"
    assert expense.description == "Lunch"


def test_invalid_date():
    with pytest.raises(ValueError, match="Invalid date format. Use DD-MM-YYYY."):
        Expense(
            "2025-02-14",
            amount=29.99,
            category="Food",
            description="Lunch",
        )


def test_to_dict():
    expense = Expense(
        date="14-02-2025",
        amount=29.99,
        category="Food",
        description="Lunch",
    )

    expense_dict = expense.to_dict()
    assert expense_dict["id"] is not None
    assert expense_dict["date"] == "14-02-2025"
    assert expense_dict["amount"] == 29.99
    assert expense_dict["category"] == "Food"
    assert expense_dict["description"] == "Lunch"


def test_from_dict():
    json_str = {
        "id": "1234",
        "date": "14-02-2025",
        "amount": 29.99,
        "category": "Food",
        "description": "Lunch",
    }

    expense = Expense.from_dict(json_str)
    assert expense.id == "1234"
    assert expense.date == "14-02-2025"
    assert expense.amount == 29.99
    assert expense.category == "Food"
    assert expense.description == "Lunch"
