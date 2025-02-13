import uuid
from datetime import datetime
import json


class Expense:

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

    def to_json(self) -> str:
        return json.dumps(self.__dict__)

    @classmethod
    def from_json(cls, json_str: str):
        data = json.loads(json_str)
        return cls(**data)

    def __str__(self):
        return f"Expense(id={self.id}, date={self.date}, amount={self.amount}, category={self.category}, description={self.description})"
