class InvalidEntryType(Exception):
    @staticmethod
    def get_message() -> str:
        return "An entry must be a Debit or a Credit object"
