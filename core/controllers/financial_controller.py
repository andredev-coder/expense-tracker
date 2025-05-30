from core.services import TransactionService
from core.views import ApplicationView
from core.models import Transaction, Transactions, TransactionType
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

        self.refresh_numbers()
        self.refresh_transaction_list()
        

    def run(self):
        pass

    def refresh_numbers(self):
        self.view.balance.value = f'${self.calculate_cards(True) + self.calculate_cards()}'
        self.view.expense_card.set_amount(self.calculate_cards())
        self.view.income_card.set_amount(self.calculate_cards(True))

        self.view.page.update()

    def refresh_transaction_list(self, transactions: Transactions | None = None):
        if not transactions:
            transactions = self.transaction_service.get_all()

        for transaction in transactions:
            self.view.transaction_list.add_transaction_card(
                transaction.id,
                transaction.type,
                transaction.description,
                transaction.date,
                transaction.amount
            )


    def add_transaction(self, amount: float, description: str):
        if amount < 0:
            transaction_type = TransactionType.EXPENSE
        else:
            transaction_type = TransactionType.INCOME

        transaction = Transaction(
            id=str(random.randint(1000, 9999)),
            type=transaction_type,
            amount=amount,
            description=description
        )
        self.transaction_service.add(transaction)

        self.refresh_numbers()
        self.refresh_transaction_list(Transactions([transaction]))


    def remove_transaction(self, transaction_id: str):
        self.transaction_service.delete(transaction_id)
        
        self.refresh_numbers()


    def calculate_cards(self, is_income: bool = False) -> float:
        return self.transaction_service.get_summary_amount(is_income)

