import unittest

from financial_accounting.main.accounts.equity import Equity


class TestAsset(unittest.TestCase):
    def test_repr_works(self) -> None:
        equity: Equity = Equity()
        self.assertEqual(first="Equity", second=equity.__repr__())

    def test_str_works(self) -> None:
        equity: Equity = Equity()
        self.assertEqual(first="Equity", second=equity.__str__())

    def test_is_asset_works(self) -> None:
        equity: Equity = Equity()
        self.assertFalse(equity.is_asset())

    def test_is_liability_works(self) -> None:
        equity: Equity = Equity()
        self.assertFalse(equity.is_liability())

    def test_is_equity_works(self) -> None:
        equity: Equity = Equity()
        self.assertTrue(equity.is_equity())


if __name__ == '__main__':
    unittest.main()
