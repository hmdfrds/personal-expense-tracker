import uuid
from datetime import datetime
import json
from dataclasses import dataclass, asdict

@dataclass
class Expense:
    id: str
    date: str
    amount: float
    category: str
    description: str

    def __init__(
        self, date: str, amount: float, category: str, description: str, id: str = None
    ):
        self.id = id if id else str(uuid.uuid4())
        self.date = self.validate_date(date)
        self.amount = amount
        self.category = category
        self.description = description

    @staticmethod
    def validate_date(date_str: str) -> str:
        try:
            datetime.strptime(date_str, "%d-%m-%Y")
            return date_str
        except ValueError:
            raise ValueError("Invalid date format. Use DD-MM-YYYY.")
    def to_dict(self):
        return asdict(self)

    @staticmethod
    def from_dict(data: dict):
        return Expense(
            id=data["id"],
            date=data["date"],
            amount=data["amount"],
            category=data["category"],
            description=data["description"],
        )