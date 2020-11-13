from collections import OrderedDict
from typing import List
from typing import OrderedDict as OrderedDictType

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.exceptions import DuplicateTransaction, InvalidTransaction, NotATransaction
from financial_accounting.main.balance_sheet.get_account.get_account import get_account, AccountDebitsAndCredits
from financial_accounting.main.balance_sheet.get_entries.get_entries import get_entries
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class BalanceSheet:
    def __init__(self):
        self.__transactions: OrderedDict[Identifier, Transaction] = OrderedDict()

    def get_transactions(self) -> OrderedDictType[Identifier, Transaction]:
        return self.__transactions

    def add_transaction(self, transaction: Transaction) -> None:
        if not isinstance(transaction, Transaction):
            raise NotATransaction(attempted_transaction=transaction)

        if transaction.get_identifier() in self.__transactions:
            raise DuplicateTransaction(transaction=transaction)

        if transaction.is_valid():
            self.__transactions[transaction.get_identifier()] = transaction
        else:
            raise InvalidTransaction(transaction=transaction)

    def get_debits(self) -> List[Debit]:
        return get_entries(transactions=[t for t in self.get_transactions().values()], entry_type=Debit)

    def get_credits(self) -> List[Credit]:
        return get_entries(transactions=[t for t in self.get_transactions().values()], entry_type=Credit)

    def get_assets(self) -> AccountDebitsAndCredits:
        return get_account(debits=self.get_debits(), credits=self.get_credits(), account_type=Asset)

    def get_liabilities(self) -> AccountDebitsAndCredits:
        return get_account(debits=self.get_debits(), credits=self.get_credits(), account_type=Liability)

    def get_equities(self) -> AccountDebitsAndCredits:
        return get_account(debits=self.get_debits(), credits=self.get_credits(), account_type=Equity)
