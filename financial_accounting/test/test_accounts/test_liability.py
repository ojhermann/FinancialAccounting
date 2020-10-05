import unittest

from financial_accounting.main.accounts.liability import Liability


class TestAsset(unittest.TestCase):
    def test_repr_works(self) -> None:
        liability: Liability = Liability()
        self.assertEqual(first="Liability", second=liability.__repr__())

    def test_str_works(self) -> None:
        liability: Liability = Liability()
        self.assertEqual(first="Liability", second=liability.__str__())

    def test_is_asset_works(self) -> None:
        liability: Liability = Liability()
        self.assertFalse(liability.is_asset())

    def test_is_liability_works(self) -> None:
        liability: Liability = Liability()
        self.assertTrue(liability.is_liability())

    def test_is_equity_works(self) -> None:
        liability: Liability = Liability()
        self.assertFalse(liability.is_equity())


if __name__ == '__main__':
    unittest.main()
