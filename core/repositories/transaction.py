import orjson
from typing import List

from core.models import Storage, Transaction, Transactions


class TransactionRepository:
    def __init__(self):
        self.storage = Storage()

    def add(self, transaction: Transaction) -> None:
        transactions = self.get_all()
        transactions.append(transaction)

        self.storage.insert(
            *[transaction.model_dump() for transaction in transactions]
        )

    def get(self, id: str) -> Transaction:
        raise NotImplementedError()

    def get_all(self) -> Transactions:
        transactions = []
        try:
            for transaction in orjson.loads(self.storage.read())['transactions']:
                transactions.append(
                    Transaction.model_validate(transaction)
                )
        except Exception as e:
            print(f'{e}')
        return Transactions(transactions)

    def delete(self, id: str) -> None:
        transactions = self.get_all()
        for transaction in transactions:
            if transaction.id == id:
                transactions.remove(
                    transaction
                )
        self.storage.insert(
            *[transaction.model_dump() for transaction in transactions]
        )


