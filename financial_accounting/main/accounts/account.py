class Account(object):
    def __repr__(self) -> str:
        return self.__class__.__name__

    def __str__(self) -> str:
        return self.__repr__()

    @staticmethod
    def is_asset() -> bool:
        return False

    @staticmethod
    def is_liability() -> bool:
        return False

    @staticmethod
    def is_equity() -> bool:
        return False

    @classmethod
    def get_name(cls) -> str:
        return cls.__name__
