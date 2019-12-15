class Account:
    def __init__(self,
                 name: str):
        self.__name = name

    def getName(self) -> str:
        return self.__name

    def getType(self) -> str:
        return self.__class__.__name__


class Asset(Account):
    def __init__(self, name: str):
        super().__init__(name)


class Liability(Account):
    def __init__(self, name: str):
        super().__init__(name)


class Equity(Account):
    def __init__(self, name: str):
        super().__init__(name)
