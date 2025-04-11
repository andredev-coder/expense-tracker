

from core.services import TransactionService
from core.views import ApplicationView
from core.models import Storage, Transaction
from core.models.transactions import TransactionType
import random

from flet import (  # type: ignore
    Dismissible
)


class FinancialController:
    def __init__(self, transaction_service: TransactionService, view: ApplicationView):
        self.transaction_service = transaction_service
        self.view = view

        self.view.transaction_form.callback = self.add_transaction
        self.view.transaction_list.on_transaction_card_dismiss = self.remove_transaction
        self.view.expense_card.set_amount(self.calculate_cards())
        self.view.income_card.set_amount(self.calculate_cards(True))

        transactions = self.transaction_service.get_all()
        for transaction in transactions:
            self.view.transaction_list.add_transaction_card(
                transaction.id,
                transaction.type,
                transaction.description,
                transaction.date,
                transaction.amount
            )



    def run(self):
        pass

    def add_transaction(self, amount: float, description: str):
        if amount < 0:
            transaction_type = TransactionType.EXPENSE
        else:
            transaction_type = TransactionType.INCOME

        transaction = Transaction(
            id=str(random.randint(1000, 9999)),
            type=transaction_type,
            amount=amount,
            category=description,
            description=description
        )
        self.transaction_service.add(transaction)

        self.view.expense_card.set_amount(self.calculate_cards())
        self.view.income_card.set_amount(self.calculate_cards(True))
        self.view.transaction_list.add_transaction_card(
            transaction.id,
            transaction.type,
            transaction.description,
            transaction.date,
            transaction.amount
        )

    def remove_transaction(self, transaction_id: str):
        self.transaction_service.delete(transaction_id)
        
        self.view.expense_card.set_amount(self.calculate_cards())
        self.view.income_card.set_amount(self.calculate_cards(True))



    def calculate_cards(self, is_income: bool = False) -> float:
        return self.transaction_service.get_summary_amount(is_income)

