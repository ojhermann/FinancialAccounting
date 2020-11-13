import unittest

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.get_entries.exceptions import InvalidEntryType
from financial_accounting.main.balance_sheet.get_entries.get_entries import get_entries
from financial_accounting.main.entries.accounting_periods.accounting_periods import AccountingPeriods
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.entries.entry import Entry
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class TestGetEntries(unittest.TestCase):
    debit_one: Debit = Debit(account_type=Asset,
                             unit="USD",
                             value=100,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q1)
    debit_two: Debit = Debit(account_type=Asset,
                             unit="USD",
                             value=50,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q1)

    credit_one: Credit = Credit(account_type=Liability,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q1)
    credit_two: Credit = Credit(account_type=Liability,
                                unit="USD",
                                value=50,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q1)

    identifier_one: Identifier = Identifier("id_one")
    transaction_one: Transaction = Transaction(identifier=identifier_one)
    transaction_one.add(debit_one)
    transaction_one.add(debit_two)
    transaction_one.add(credit_one)
    transaction_one.add(credit_two)

    identifier_two: Identifier = Identifier("id_two")
    transaction_two: Transaction = Transaction(identifier=identifier_two)
    transaction_two.add(debit_one)
    transaction_two.add(debit_two)
    transaction_two.add(credit_one)
    transaction_two.add(credit_two)

    def test_it_works_with_an_empty_list(self) -> None:
        self.assertEqual(get_entries(transactions=[], entry_type=Debit), [])
        self.assertEqual(get_entries(transactions=[], entry_type=Credit), [])

    def test_it_works_for_debits(self) -> None:
        self.assertEqual(get_entries(transactions=[TestGetEntries.transaction_one, TestGetEntries.transaction_two],
                                     entry_type=Debit),
                         [TestGetEntries.debit_two,
                          TestGetEntries.debit_two,
                          TestGetEntries.debit_one,
                          TestGetEntries.debit_one])

    def test_it_works_for_credits(self) -> None:
        self.assertEqual(get_entries(transactions=[TestGetEntries.transaction_one, TestGetEntries.transaction_two],
                                     entry_type=Credit),
                         [TestGetEntries.credit_two,
                          TestGetEntries.credit_two,
                          TestGetEntries.credit_one,
                          TestGetEntries.credit_one])

    def test_it_will_raise_invalid_entry_type(self) -> None:
        entry: Entry = Entry(account_type=Liability,
                             unit="USD",
                             value=50,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q1)

        bogus_values: list = ["", "1", "2.0", 1, 10, 100, 1.0, 10.5, 35.67, entry]
        for bogus_value in bogus_values:
            self.assertRaises(InvalidEntryType,
                              get_entries,
                              [TestGetEntries.transaction_one, TestGetEntries.transaction_two],
                              bogus_value)
