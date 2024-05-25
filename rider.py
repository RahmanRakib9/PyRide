# rider.py
from user import User
from ride import Ride


class Rider(User):
    def __init__(self, name, email, nationalId, initialAmount):
        super().__init__(name, email, nationalId)
        self.wallet = initialAmount
        self.currentRide = None

    def requestRide(self, rideSharing, destination):
        if not self.currentRide:
            for driver in rideSharing.drivers:
                if driver.isAvailable():
                    self.currentRide = Ride(self, driver, destination)
                    rideSharing.rides.append(self.currentRide)
                    driver.currentRide = self.currentRide
                    print(
                        f'Ride requested by {self.name} destination is {destination} with driver {driver.name}')
                    break
            else:
                print("No available drivers at the moment.")
