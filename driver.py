# driver.py
from user import User


class Driver(User):
    def __init__(self, name, email, nationalId):
        super().__init__(name, email, nationalId)
        self.currentRide = None

    def isAvailable(self):
        return self.currentRide is None
