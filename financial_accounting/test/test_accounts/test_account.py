import unittest

from financial_accounting.main.accounts.account import Account


class TestAccount(unittest.TestCase):
    def test_repr_works(self) -> None:
        account: Account = Account()
        self.assertEqual(first="Account", second=account.__repr__())

    def test_str_works(self) -> None:
        account: Account = Account()
        self.assertEqual(first="Account", second=account.__str__())

    def test_is_asset_works(self) -> None:
        account: Account = Account()
        self.assertFalse(account.is_asset())

    def test_is_liability_works(self) -> None:
        account: Account = Account()
        self.assertFalse(account.is_liability())

    def test_is_equity_works(self) -> None:
        account: Account = Account()
        self.assertFalse(account.is_equity())


if __name__ == '__main__':
    unittest.main()
