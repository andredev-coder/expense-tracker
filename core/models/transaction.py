from pydantic import BaseModel, Field
from datetime import datetime
from enum import StrEnum

from typing import Optional, Self


class TransactionType(StrEnum):
    EXPENSE = 'expense'
    INCOME = 'income'


class Transaction(BaseModel):
    id: str
    type: TransactionType
    amount: float
    date: datetime = Field(default_factory=datetime.now)
    description: Optional[str] = None

    @property
    def is_income(self) -> bool:
        return self.type == TransactionType.INCOME
    

class Transactions(list[Transaction]):
    def select(self, transaction_type: TransactionType) -> Self:
        return self.__class__([
            transaction for transaction in self
            if transaction.type == transaction_type
        ])
    
    def total_expenses(self) -> float:
        return sum(
            transaction.amount for transaction in self
            if not transaction.is_income
        )
    
    def total_income(self) -> float:
        return sum(
            transaction.amount for transaction in self
            if transaction.is_income
        )