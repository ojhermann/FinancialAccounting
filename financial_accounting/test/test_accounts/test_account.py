import unittest
from financial_accounting.main.accounts.account import Account, Asset, Liability, Equity


class TestAccounts(unittest.TestCase):
    def testAccountWorks(self):
        self.assertEqual(
            object.__name__,
            Account.getAccountType())

        self.assertEqual(
            Account.__name__,
            Account.getAccount())

    def testAssetWorks(self):
        self.assertEqual(
            Account.__name__,
            Asset.getAccountType())

        self.assertEqual(
            Asset.__name__,
            Asset.getAccount())

        class AccountsReceivable(Asset):
            pass

        self.assertEqual(
            Asset.__name__,
            AccountsReceivable.getAccountType())

        self.assertEqual(
            AccountsReceivable.__name__,
            AccountsReceivable.getAccount())

    def testLiabilityWorks(self):
        self.assertEqual(
            Account.__name__,
            Liability.getAccountType())

        self.assertEqual(
            Liability.__name__,
            Liability.getAccount())

        class AccountsPayable(Liability):
            pass

        self.assertEqual(
            Liability.__name__,
            AccountsPayable.getAccountType())

        self.assertEqual(
            AccountsPayable.__name__,
            AccountsPayable.getAccount())

    def testEquityWorks(self):
        self.assertEqual(
            Account.__name__,
            Equity.getAccountType())

        self.assertEqual(
            Equity.__name__,
            Equity.getAccount())

        class RetainedEarnings(Equity):
            pass

        self.assertEqual(
            Equity.__name__,
            RetainedEarnings.getAccountType())

        self.assertEqual(
            RetainedEarnings.__name__,
            RetainedEarnings.getAccount())


if __name__ == '__main__':
    unittest.main()
