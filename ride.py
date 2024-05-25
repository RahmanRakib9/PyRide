from datetime import datetime

class Ride:
    def __init__(self, rider, driver, destination):
        self.rider = rider
        self.driver = driver
        self.startLocation = rider.currentLocation
        self.destination = destination
        self.startTime = datetime.now()

    def endRide(self):
        self.endTime = datetime.now()
        self.rider.currentRide = None
        self.driver.currentRide = None
        print(f'Ride started from {self.startLocation} to {self.destination} ended.')
