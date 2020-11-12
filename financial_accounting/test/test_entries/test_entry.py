import unittest
from datetime import datetime
from typing import List

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.entries.accounting_periods.accounting_periods import AccountingPeriods
from financial_accounting.main.entries.entry import Entry


class TestEntry(unittest.TestCase):
    unit: str = "USD"
    asset_value: int = 100
    liability_value: int = 50
    equity_value: int = 50
    year: int = 2020
    month: int = 10
    day: int = 10
    entry_asset: Entry = Entry(account_type=Asset,
                               unit=unit,
                               value=asset_value,
                               year=year,
                               month=month,
                               day=day,
                               accounting_period=AccountingPeriods.Q1)
    entry_liability: Entry = Entry(account_type=Liability,
                                   unit=unit,
                                   value=liability_value,
                                   year=year,
                                   month=month,
                                   day=day,
                                   accounting_period=AccountingPeriods.Q1)
    entry_equity: Entry = Entry(account_type=Equity,
                                unit=unit,
                                value=equity_value,
                                year=year,
                                month=month,
                                day=day,
                                accounting_period=AccountingPeriods.Q1)

    @staticmethod
    def get_test_entries() -> List[Entry]:
        return [TestEntry.entry_asset, TestEntry.entry_liability, TestEntry.entry_equity]

    def test_repr_works(self) -> None:
        for entry in TestEntry.get_test_entries():
            self.assertEqual(
                "Entry",
                entry.__repr__())

    def test_str_works(self) -> None:
        for entry in TestEntry.get_test_entries():
            self.assertEqual(
                "Entry",
                entry.__str__())

    def test__get_value_will_raise_type_error_for_non_ints(self) -> None:
        for value in [1.50, 0.0, "1.50", "0.0", "hello", None]:
            self.assertRaises(
                TypeError,
                Entry._get_value,
                value=value)
            for account_type in [Asset, Liability, Equity]:
                self.assertRaises(
                    TypeError,
                    Entry,
                    account_type=account_type, unit="USD", value=value, year=2020, month=10, day=10,
                    accounting_period=AccountingPeriods.Q1)

    def test__get_value_will_raise_value_error_for_negative_ints(self) -> None:
        for value in [-100, -36, -1]:
            self.assertRaises(
                ValueError,
                Entry._get_value,
                value=value)
            for account_type in [Asset, Liability, Equity]:
                self.assertRaises(
                    ValueError,
                    Entry,
                    account_type=account_type, unit="USD", value=value, year=2020, month=10, day=10,
                    accounting_period=AccountingPeriods.Q1)

    def test_is_debit_works(self) -> None:
        self.assertFalse(Entry.is_debit())

    def test_is_credit_works(self) -> None:
        self.assertFalse(Entry.is_credit())

    def test_get_account_works(self) -> None:
        self.assertEqual(Asset, TestEntry.entry_asset.get_account())
        self.assertEqual(Liability, TestEntry.entry_liability.get_account())
        self.assertEqual(Equity, TestEntry.entry_equity.get_account())

    def test_get_unit_works(self) -> None:
        self.assertEqual(TestEntry.unit, TestEntry.entry_asset.get_unit())
        self.assertEqual(TestEntry.unit, TestEntry.entry_liability.get_unit())
        self.assertEqual(TestEntry.unit, TestEntry.entry_equity.get_unit())

    def test_get_value_works(self) -> None:
        self.assertEqual(TestEntry.asset_value, TestEntry.entry_asset.get_value())
        self.assertEqual(TestEntry.liability_value, TestEntry.entry_liability.get_value())
        self.assertEqual(TestEntry.equity_value, TestEntry.entry_equity.get_value())

    def test_get_date_works(self) -> None:
        expected_date: datetime = datetime(year=TestEntry.year, month=TestEntry.month, day=TestEntry.day)
        self.assertEqual(expected_date, TestEntry.entry_asset.get_date())
        self.assertEqual(expected_date, TestEntry.entry_liability.get_date())
        self.assertEqual(expected_date, TestEntry.entry_equity.get_date())


if __name__ == '__main__':
    unittest.main()
