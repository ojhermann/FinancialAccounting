from typing import Dict

from financial_accounting.main.balance_sheet.exceptions import DuplicateTransaction, InvalidTransaction
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class BalanceSheet:
    def __init__(self):
        self.__transactions: Dict[Identifier, Transaction] = dict()

    def get_transactions(self) -> Dict[Identifier, Transaction]:
        return self.__transactions

    def add_transaction(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise TypeError("Only Transaction objects can be added to a balance sheet")

        if transaction.get_identifier() in self.__transactions:
            raise DuplicateTransaction(transaction=transaction)

        if transaction.is_valid():
            self.__transactions[transaction.get_identifier()] = transaction
        else:
            raise InvalidTransaction(transaction=transaction)
