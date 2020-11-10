import unittest
from typing import List

from financial_accounting.main.transactions.identifier import Identifier


class TestIdentifier(unittest.TestCase):
    def test_it_will_raise_type_error(self) -> None:
        bogus_values: list = [0, 1, 0.0, 1.1, True, False]
        for bogus_value in bogus_values:
            self.assertRaises(TypeError, Identifier, bogus_value)

    def test_it_will_raise_value_error(self) -> None:
        bogus_values: list = ["", " ", "    "]
        for bogus_value in bogus_values:
            self.assertRaises(ValueError, Identifier, bogus_value)

    def test_it_works_as_a_string(self) -> None:
        values: List[str] = ["This_should_work", "This should work"]
        for value in values:
            identifier: Identifier = Identifier(value=value)
            self.assertEqual(identifier, value)


if __name__ == '__main__':
    unittest.main()
