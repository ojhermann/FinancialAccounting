import unittest

from financial_accounting.main.entries.debit import Debit


class TestDebit(unittest.TestCase):
    def test_get_debit_works(self) -> None:
        self.assertTrue(Debit.is_debit())

    def test_get_credit_works(self) -> None:
        self.assertFalse(Debit.is_credit())


if __name__ == '__main__':
    unittest.main()
