import unittest

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.balance_sheet import BalanceSheet
from financial_accounting.main.balance_sheet.exceptions import DuplicateTransaction, InvalidTransaction
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class TestAddTransaction(unittest.TestCase):
    def test_it_will_raise_type_error(self) -> None:
        balance_sheet: BalanceSheet = BalanceSheet()
        bogus_values: list = ["", "1", "2.0", 1, 10, 100, 1.0, 10.5, 35.67, True, False]
        for bogus_value in bogus_values:
            self.assertRaises(TypeError, balance_sheet.add_transaction, bogus_value)

    def test_it_will_raise_for_a_duplicate_transaction(self) -> None:
        debit: Debit = Debit(account_type=Asset, unit="USD", value=100, year=2020, month=11, day=10)
        credit: Credit = Credit(account_type=Liability, unit="USD", value=100, year=2020, month=11, day=10)

        identifier: Identifier = Identifier("This is the identifier")

        transaction: Transaction = Transaction(identifier=identifier)
        transaction.add(debit)
        transaction.add(credit)

        balance_sheet: BalanceSheet = BalanceSheet()
        balance_sheet.add_transaction(transaction=transaction)

        self.assertRaises(DuplicateTransaction, balance_sheet.add_transaction, transaction)

    def test_it_will_raise_for_an_invalid_transaction(self) -> None:
        identifier: Identifier = Identifier("This is the identifier")

        transaction: Transaction = Transaction(identifier=identifier)

        balance_sheet: BalanceSheet = BalanceSheet()

        self.assertRaises(InvalidTransaction, balance_sheet.add_transaction, transaction)

    def test_it_works(self) -> None:
        debit: Debit = Debit(account_type=Asset, unit="USD", value=100, year=2020, month=11, day=10)
        credit: Credit = Credit(account_type=Liability, unit="USD", value=100, year=2020, month=11, day=10)

        identifier: Identifier = Identifier("This is the identifier")

        transaction: Transaction = Transaction(identifier=identifier)
        transaction.add(debit)
        transaction.add(credit)

        balance_sheet: BalanceSheet = BalanceSheet()
        balance_sheet.add_transaction(transaction=transaction)

        self.assertEqual(balance_sheet.get_transactions(), {identifier: transaction})
