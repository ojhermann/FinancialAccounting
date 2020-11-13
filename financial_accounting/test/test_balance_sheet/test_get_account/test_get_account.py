import unittest

from financial_accounting.main.accounts.asset import Asset
from financial_accounting.main.accounts.equity import Equity
from financial_accounting.main.accounts.liability import Liability
from financial_accounting.main.balance_sheet.get_account.get_account import get_account, AccountDebitsAndCredits
from financial_accounting.main.entries.accounting_periods.accounting_periods import AccountingPeriods
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.identifier import Identifier
from financial_accounting.main.transactions.transaction import Transaction


class TestGetAccount(unittest.TestCase):
    debit_asset: Debit = Debit(account_type=Asset,
                               unit="USD",
                               value=100,
                               year=2020,
                               month=11,
                               day=10,
                               accounting_period=AccountingPeriods.Q1)
    debit_liability: Debit = Debit(account_type=Liability,
                                   unit="USD",
                                   value=100,
                                   year=2020,
                                   month=11,
                                   day=10,
                                   accounting_period=AccountingPeriods.Q1)
    debit_equity: Debit = Debit(account_type=Equity,
                                unit="USD",
                                value=100,
                                year=2020,
                                month=11,
                                day=10,
                                accounting_period=AccountingPeriods.Q1)

    credit_asset: Credit = Credit(account_type=Asset,
                                  unit="USD",
                                  value=100,
                                  year=2020,
                                  month=11,
                                  day=10,
                                  accounting_period=AccountingPeriods.Q1)
    credit_liability: Credit = Credit(account_type=Liability,
                                      unit="USD",
                                      value=100,
                                      year=2020,
                                      month=11,
                                      day=10,
                                      accounting_period=AccountingPeriods.Q1)
    credit_equity: Credit = Credit(account_type=Equity,
                                   unit="USD",
                                   value=100,
                                   year=2020,
                                   month=11,
                                   day=10,
                                   accounting_period=AccountingPeriods.Q1)

    identifier: Identifier = Identifier("This is the identifier")
    transaction: Transaction = Transaction(identifier=identifier)
    transaction.add(debit_asset)
    transaction.add(debit_liability)
    transaction.add(debit_equity)
    transaction.add(credit_asset)
    transaction.add(credit_liability)
    transaction.add(credit_equity)

    def test_it_works_with_empty_lists(self) -> None:
        self.assertEqual(get_account(debits=[], credits=[], account_type=Asset),
                         AccountDebitsAndCredits(debits=[], credits=[]))
        self.assertEqual(get_account(debits=[], credits=[], account_type=Liability),
                         AccountDebitsAndCredits(debits=[], credits=[]))
        self.assertEqual(get_account(debits=[], credits=[], account_type=Equity),
                         AccountDebitsAndCredits(debits=[], credits=[]))

    def test_it_works_for_assets(self) -> None:
        self.assertEqual(
            get_account(debits=TestGetAccount.transaction.get_debits(),
                        credits=TestGetAccount.transaction.get_credits(),
                        account_type=Asset),
            AccountDebitsAndCredits(debits=[TestGetAccount.debit_asset], credits=[TestGetAccount.credit_asset]))

    def test_it_works_for_liabilities(self) -> None:
        self.assertEqual(
            get_account(debits=TestGetAccount.transaction.get_debits(),
                        credits=TestGetAccount.transaction.get_credits(),
                        account_type=Liability),
            AccountDebitsAndCredits(debits=[TestGetAccount.debit_liability], credits=[TestGetAccount.credit_liability]))

    def test_it_works_for_equities(self) -> None:
        self.assertEqual(
            get_account(debits=TestGetAccount.transaction.get_debits(),
                        credits=TestGetAccount.transaction.get_credits(),
                        account_type=Equity),
            AccountDebitsAndCredits(debits=[TestGetAccount.debit_equity], credits=[TestGetAccount.credit_equity]))
