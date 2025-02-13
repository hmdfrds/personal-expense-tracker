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


def test_to_json():
    expense = Expense(
        date="14-02-2025",
        amount=29.99,
        category="Food",
        description="Lunch",
    )

    json_data = expense.to_json()
    data = json.loads(json_data)

    assert data["id"] is not None
    assert data["date"] == "14-02-2025"
    assert data["amount"] == 29.99
    assert data["category"] == "Food"
    assert data["description"] == "Lunch"


def test_from_json():
    json_str = json.dumps(
        {
            "id": "1234",
            "date": "14-02-2025",
            "amount": 29.99,
            "category": "Food",
            "description": "Lunch",
        }
    )

    expense = Expense.from_json(json_str)

    assert expense.id == "1234"
    assert expense.date == "14-02-2025"
    assert expense.amount == 29.99
    assert expense.category == "Food"
    assert expense.description == "Lunch"
