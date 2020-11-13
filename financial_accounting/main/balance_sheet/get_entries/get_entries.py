from typing import Union, Type, List

from financial_accounting.main.balance_sheet.get_entries.exceptions import InvalidEntryType
from financial_accounting.main.entries.credit import Credit
from financial_accounting.main.entries.debit import Debit
from financial_accounting.main.transactions.transaction import Transaction


def get_entries(transactions: List[Transaction],
                entry_type: Union[Type[Debit], Type[Credit]]) -> List[Union[Debit, Credit]]:
    if entry_type == Debit:
        entries = [entry for entries in [t.get_debits() for t in transactions] for entry in entries]
    elif entry_type == Credit:
        entries = [entry for entries in [t.get_credits() for t in transactions] for entry in entries]
    else:
        raise InvalidEntryType()

    entries.sort(key=lambda e: (e.get_accounting_period(), e.get_date(), e.get_value()))

    return entries
