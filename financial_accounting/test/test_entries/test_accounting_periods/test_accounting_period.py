import unittest
from typing import List

from financial_accounting.main.entries.accounting_periods.accounting_periods import AccountingPeriod, AccountingPeriods


class TestAccountingPeriod(unittest.TestCase):
    def test_it_will_raise_type_error(self) -> None:
        bogus_values: list = [0, 1, 0.0, 1.1, True, False]
        for bogus_value in bogus_values:
            self.assertRaises(TypeError, AccountingPeriod, bogus_value)

    def test_it_will_raise_value_error(self) -> None:
        bogus_values: list = ["", " ", "    "]
        for bogus_value in bogus_values:
            self.assertRaises(ValueError, AccountingPeriod, bogus_value)

    def test_it_works_as_a_string(self) -> None:
        values: List[str] = ["Q1", "Q2"]
        for value in values:
            accounting_period: AccountingPeriod = AccountingPeriod(value=value)
            self.assertEqual(accounting_period, value)


class TestAccountingPeriods(unittest.TestCase):
    def test_order_is_correct(self) -> None:
        self.assertTrue(AccountingPeriods.Q1 < AccountingPeriods.Q2)
        self.assertTrue(AccountingPeriods.Q2 < AccountingPeriods.Q3)
        self.assertTrue(AccountingPeriods.Q3 < AccountingPeriods.Q4)
