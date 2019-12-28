class Account:
    @classmethod
    def getAccountType(cls) -> str:
        return cls.__base__.__name__

    @classmethod
    def getAccountName(cls) -> str:
        return cls.__name__


class Asset(Account):
    pass


class Liability(Account):
    pass


class Equity(Account):
    pass
