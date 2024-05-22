from abc import ABC, abstractmethod


class USer(ABC):
    def __init__(self, name, email, nationalId) -> None:
        self.name = name
        self.email = email
        # TODO : generate id dynamically
        self.__id = 0
        self.__nationalId = nationalId
        self.__wallet = 0

    @abstractmethod
    def displayProfile(self):
        raise NotImplementedError
