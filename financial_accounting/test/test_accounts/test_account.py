import unittest
from financial_accounting.main.accounts.account import Account, Asset, Liability, Equity


class TestAccounts(unittest.TestCase):
    def testAssetWorks(self):
        self.assertEqual(
            Account.__name__,
            Asset.getAccountType())

        self.assertEqual(
            Asset.__name__,
            Asset.getAccountName())

        class AccountsReceivable(Asset):
            pass

        self.assertEqual(
            Asset.__name__,
            AccountsReceivable.getAccountType())

        self.assertEqual(
            AccountsReceivable.__name__,
            AccountsReceivable.getAccountName())

    def testLiabilityWorks(self):
        self.assertEqual(
            Account.__name__,
            Liability.getAccountType())

        self.assertEqual(
            Liability.__name__,
            Liability.getAccountName())

        class AccountsPayable(Liability):
            pass

        self.assertEqual(
            Liability.__name__,
            AccountsPayable.getAccountType())

        self.assertEqual(
            AccountsPayable.__name__,
            AccountsPayable.getAccountName())

    def testEquityWorks(self):
        self.assertEqual(
            Account.__name__,
            Equity.getAccountType())

        self.assertEqual(
            Equity.__name__,
            Equity.getAccountName())

        class RetainedEarnings(Equity):
            pass

        self.assertEqual(
            Equity.__name__,
            RetainedEarnings.getAccountType())

        self.assertEqual(
            RetainedEarnings.__name__,
            RetainedEarnings.getAccountName())


if __name__ == '__main__':
    unittest.main()
