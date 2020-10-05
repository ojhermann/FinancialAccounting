import unittest

from financial_accounting.main.accounts.asset import Asset


class TestAsset(unittest.TestCase):
    def test_repr_works(self) -> None:
        asset: Asset = Asset()
        self.assertEqual(first="Asset", second=asset.__repr__())

    def test_str_works(self) -> None:
        asset: Asset = Asset()
        self.assertEqual(first="Asset", second=asset.__str__())

    def test_is_asset_works(self) -> None:
        asset: Asset = Asset()
        self.assertTrue(asset.is_asset())

    def test_is_liability_works(self) -> None:
        asset: Asset = Asset()
        self.assertFalse(asset.is_liability())

    def test_is_equity_works(self) -> None:
        asset: Asset = Asset()
        self.assertFalse(asset.is_equity())


if __name__ == '__main__':
    unittest.main()
