import unittest
from financial_accounting.main.accounts import AccountType, Account, Asset, Liability, Equity


class TestAccounts(unittest.TestCase):
    def testAccountWorks(self):
        self.assertEqual(
            Account.getType(),
            AccountType.account)

        self.assertEqual(
            Account.getName(),
            'Account')

    def testAssetWorks(self):
        class AccountsReceivable(Asset):
            pass

        self.assertEqual(
            AccountsReceivable.getType(),
            AccountType.asset)

        self.assertEqual(
            AccountsReceivable.getName(),
            'AccountsReceivable')

    def testLiabilitiesWorks(self):
        class AccountsPayable(Liability):
            pass

        self.assertEqual(
            AccountsPayable.getType(),
            AccountType.liability)

        self.assertEqual(
            AccountsPayable.getName(),
            'AccountsPayable')

    def testEquityWorks(self):
        class RetainedEarnings(Equity):
            pass

        self.assertEqual(
            RetainedEarnings.getType(),
            AccountType.equity)

        self.assertEqual(
            RetainedEarnings.getName(),
            'RetainedEarnings')


if __name__ == '__main__':
    unittest.main()
