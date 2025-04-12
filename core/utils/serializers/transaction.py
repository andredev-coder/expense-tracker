import orjson
from typing import List, Dict
from core.models import Transaction, Transactions


class TransactionSerializer:
    @staticmethod
    def serialize(transactions: Transactions) -> List[Dict]:
        return [transaction.model_dump() for transaction in transactions]

    @staticmethod
    def deserialize(transactions: List[Dict]) -> Transactions:
        try:
            return Transactions([Transaction.model_validate(t) for t in transactions])
        except (orjson.JSONDecodeError, KeyError) as e:
            return Transactions([])
