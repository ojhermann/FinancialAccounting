import unittest

from financial_accounting.main.entries.credit import Credit


class TestDebit(unittest.TestCase):
    def test_get_debit_works(self) -> None:
        self.assertFalse(Credit.is_debit())

    def test_get_credit_works(self) -> None:
        self.assertTrue(Credit.is_credit())


if __name__ == '__main__':
    unittest.main()
