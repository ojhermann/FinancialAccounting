import unittest
from financial_accounting.main.accounts import Account


class TestAccounts(unittest.TestCase):
    def testAccountWorks(self):
        accountName: str = 'accountName'
        accountType: str = 'Account'
        account: Account = Account(name=accountName)

        self.assertEqual(account.getName(), accountName)

        self.assertEqual(account.getType(), accountType)


if __name__ == '__main__':
    unittest.main()
