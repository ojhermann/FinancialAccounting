import unittest

from financial_accounting.main.accounts.account import Account, Asset, Liability, Equity


class TestAccount(unittest.TestCase):
    def account_works(self,
                      account: Account,
                      representation: str) -> None:
        self.assertEqual(representation,
                         account.__repr__())

    def test_base_classes_work(self) -> None:
        self.account_works(Account(), 'Account')
        self.account_works(Asset(), 'Asset')
        self.account_works(Liability(), 'Liability')
        self.account_works(Equity(), 'Equity')

    def test_sub_classes_work(self) -> None:
        class AccountsReceivable(Asset):
            pass

        self.account_works(AccountsReceivable(), 'AccountsReceivable')

        class AccountsPayable(Liability):
            pass

        self.account_works(AccountsPayable(), 'AccountsPayable')

        class RetainedEarnings(Equity):
            pass

        self.account_works(RetainedEarnings(), 'RetainedEarnings')


if __name__ == '__main__':
    unittest.main()
