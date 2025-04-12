import flet # type: ignore
from core.views import ApplicationView
from core.controllers import FinancialController
from core.repositories import TransactionRepository
from core.services import TransactionService
from core.utils.storage import JSONFileStorage



def main(page: flet.Page):
    storage = JSONFileStorage()

    transaction_repo = TransactionRepository(storage)
    transaction_service = TransactionService(transaction_repo)

    app_view = ApplicationView(page)

    app_controller = FinancialController(transaction_service, app_view)
    app_controller.run()


flet.app(main)