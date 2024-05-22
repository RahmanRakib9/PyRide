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


class Rider(USer):
    def __init__(self, name, email, nationalId) -> None:
        super().__init__(name, email, nationalId)

    def displayProfile(self):
        print(f'Rider with name: {self.name} and email: {self.email}')

    def requestRide(self, location, destination):
        if not self.currentRide:
            # TODO: Set ride properly
            # TODO : set ride match
            ride_request = None
            self.currentRide = None
