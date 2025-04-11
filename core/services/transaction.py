from typing import List

from core.repositories import TransactionRepository
from core.models import Transaction, Expense, Income
from core.models.transactions import TransactionType
from core.models.transactions import Transactions


class TransactionService:
    def __init__(self, repository: TransactionRepository):
        self.repository = repository

    def add(self, transaction: Transaction) -> None:
        self.repository.add(transaction)

    def get(self, id: str) -> Transaction:
        raise NotImplementedError()

    def get_all(self) -> Transactions:
        return Transactions(self.repository.get_all())
    
    def delete(self, id: str) -> None:
        self.repository.delete(id)

    def get_summary_amount(self, is_income: bool = False) -> float:
        transactions = self.get_all()
        
        if is_income:
            return transactions.total_income()
        return transactions.total_expenses()
