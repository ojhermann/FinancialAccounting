import unittest

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.entries.entry import Entry
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class TestTransaction(unittest.TestCase):
    identifier: Identifier = Identifier("This is the identifier")

    transaction: Transaction = Transaction(identifier=identifier)

    debit_one: Debit = Debit(account_type=Asset, unit="USD", value=100, year=2020, month=11, day=10)
    debit_two: Debit = Debit(account_type=Asset, unit="USD", value=100, year=2020, month=11, day=10)
    transaction.add(debit_one)
    transaction.add(debit_two)

    credit_one: Credit = Credit(account_type=Liability, unit="USD", value=100, year=2020, month=11, day=10)
    credit_two: Credit = Credit(account_type=Liability, unit="USD", value=100, year=2020, month=11, day=10)
    transaction.add(credit_one)
    transaction.add(credit_two)

    def test_get_identifier_works(self) -> None:
        self.assertEqual(TestTransaction.identifier, TestTransaction.transaction.get_identifier())

    def test_it_can_get_debits(self) -> None:
        self.assertEqual(TestTransaction.transaction.get_debits(),
                         [TestTransaction.debit_one, TestTransaction.debit_two])

    def test_it_can_get_credits(self) -> None:
        self.assertEqual(TestTransaction.transaction.get_credits(),
                         [TestTransaction.credit_one, TestTransaction.credit_two])

    def test_it_can_get_debit_total_value(self) -> None:
        self.assertEqual(TestTransaction.transaction.get_debit_total_value(),
                         sum([d.get_value() for d in [TestTransaction.debit_one, TestTransaction.debit_two]]))

    def test_it_can_get_credit_total_value(self) -> None:
        self.assertEqual(TestTransaction.transaction.get_credit_total_value(),
                         sum([c.get_value() for c in [TestTransaction.credit_one, TestTransaction.credit_two]]))

    def test_is_balanced_works(self) -> None:
        self.assertTrue(TestTransaction.transaction.is_balanced())

        identifier: Identifier = Identifier("This is the identifier")
        transaction: Transaction = Transaction(identifier=identifier)
        debit_one: Debit = Debit(account_type=Asset, unit="USD", value=100, year=2020, month=11, day=10)
        transaction.add(debit_one)
        self.assertFalse(transaction.is_balanced())

        credit_one: Credit = Credit(account_type=Liability, unit="USD", value=50, year=2020, month=11, day=10)
        transaction.add(credit_one)
        self.assertFalse(transaction.is_balanced())

    def test_it_will_raise_type_error_when_adding(self) -> None:
        identifier: Identifier = Identifier("This is the identifier")
        transaction: Transaction = Transaction(identifier=identifier)

        entry: Entry = Entry(account_type=Liability, unit="USD", value=50, year=2020, month=11, day=10)

        bogus_values: list = ["", "1", "2.0", 1, 10, 100, 1.0, 10.5, 35.67, entry]
        for bogus_value in bogus_values:
            self.assertRaises(TypeError, transaction.add, bogus_value)
