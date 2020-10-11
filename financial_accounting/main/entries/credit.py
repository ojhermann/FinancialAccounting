from financial_accounting.main.entries.entry import Entry


class Credit(Entry):
    @staticmethod
    def is_credit() -> bool:
        return True
