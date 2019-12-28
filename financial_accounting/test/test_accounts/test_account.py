import unittest
from financial_accounting.main.accounts.account import Account, Asset, Liability, Equity


class TestAccounts(unittest.TestCase):
    def testAssetWorks(self):
        self.assertEqual(
            Account.__name__,
            Asset.getType())

        self.assertEqual(
            Asset.__name__,
            Asset.getName())

        class AccountsReceivable(Asset):
            pass

        self.assertEqual(
            Asset.__name__,
            AccountsReceivable.getType())

        self.assertEqual(
            AccountsReceivable.__name__,
            AccountsReceivable.getName())

    def testLiabilityWorks(self):
        self.assertEqual(
            Account.__name__,
            Liability.getType())

        self.assertEqual(
            Liability.__name__,
            Liability.getName())

        class AccountsPayable(Liability):
            pass

        self.assertEqual(
            Liability.__name__,
            AccountsPayable.getType())

        self.assertEqual(
            AccountsPayable.__name__,
            AccountsPayable.getName())

    def testEquityWorks(self):
        self.assertEqual(
            Account.__name__,
            Equity.getType())

        self.assertEqual(
            Equity.__name__,
            Equity.getName())

        class RetainedEarnings(Equity):
            pass

        self.assertEqual(
            Equity.__name__,
            RetainedEarnings.getType())

        self.assertEqual(
            RetainedEarnings.__name__,
            RetainedEarnings.getName())


if __name__ == '__main__':
    unittest.main()
