from core.models import Transaction, Transactions
from core.utils.storage import Storage
from core.utils.serializers import TransactionSerializer


class TransactionRepository:
    def __init__(self, storage: Storage):
        self.storage = storage

    def add(self, transaction: Transaction) -> None:
        transactions = self.get_all()
        transactions.append(transaction)

        self.storage.save(*TransactionSerializer.serialize(transactions))

    def get(self, id: str) -> Transaction:
        raise NotImplementedError()

    def get_all(self) -> Transactions:
        transactions = self.storage.load()
        return TransactionSerializer.deserialize(transactions)


    def delete(self, id: str) -> None:
        transactions = self.get_all()
        for transaction in transactions:
            if transaction.id == id:
                transactions.remove(
                    transaction
                )
        self.storage.save(*TransactionSerializer.serialize(transactions))


