import unittest

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.get_account.exceptions import InvalidAccountType, NotDebitOrCredit
from financial_accounting.main.balance_sheet.get_account.is_account_type import is_account_type
from financial_accounting.main.entries.accounting_periods.accounting_periods import AccountingPeriods
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.entries.entry import Entry


class TestIsAccountType(unittest.TestCase):
    def test_it_works_for_assets(self) -> None:
        debit: Debit = Debit(account_type=Asset,
                             unit="USD",
                             value=100,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q2)
        credit: Credit = Credit(account_type=Asset,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q2)
        self.assertTrue(is_account_type(entry=debit, account_type=Asset))
        self.assertTrue(is_account_type(entry=credit, account_type=Asset))

    def test_it_works_for_liabilities(self) -> None:
        debit: Debit = Debit(account_type=Liability,
                             unit="USD",
                             value=100,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q2)
        credit: Credit = Credit(account_type=Liability,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q2)
        self.assertTrue(is_account_type(entry=debit, account_type=Liability))
        self.assertTrue(is_account_type(entry=credit, account_type=Liability))

    def test_it_works_for_equities(self) -> None:
        debit: Debit = Debit(account_type=Equity,
                             unit="USD",
                             value=100,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q2)
        credit: Credit = Credit(account_type=Equity,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q2)
        self.assertTrue(is_account_type(entry=debit, account_type=Equity))
        self.assertTrue(is_account_type(entry=credit, account_type=Equity))

    def test_it_will_raise_not_debit_or_credit(self) -> None:
        entry: Entry = Entry(account_type=Liability,
                             unit="USD",
                             value=50,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q1)

        class AccountsReceivable(Asset):
            pass

        class AccountsPayable(Liability):
            pass

        class RetainedEarnings(Equity):
            pass

        for account_type in [Asset, Liability, Equity, AccountsReceivable, AccountsPayable, RetainedEarnings]:
            self.assertRaises(NotDebitOrCredit,
                              is_account_type,
                              entry,
                              account_type)

    def test_it_will_raise_invalid_account_type(self) -> None:
        debit: Debit = Debit(account_type=Equity,
                             unit="USD",
                             value=100,
                             year=2020,
                             month=11,
                             day=10,
                             accounting_period=AccountingPeriods.Q2)
        credit: Credit = Credit(account_type=Equity,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q2)

        bogus_values: list = [str, int, bool, float]
        for bogus_value in bogus_values:
            for entry in [debit, credit]:
                self.assertRaises(InvalidAccountType,
                                  is_account_type,
                                  entry,
                                  bogus_value)
