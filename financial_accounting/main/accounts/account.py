class Account:
    @classmethod
    def getType(cls) -> str:
        return cls.__base__.__name__

    @classmethod
    def getAccount(cls) -> str:
        return cls.__name__


class Asset(Account):
    pass


class Liability(Account):
    pass


class Equity(Account):
    pass
