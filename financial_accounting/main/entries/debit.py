from financial_accounting.main.entries.entry import Entry


class Debit(Entry):
    @staticmethod
    def is_debit() -> bool:
        return True
