from datetime import datetime


class RideSharing:
    def __init__(self, companyName):
        self.companyName = companyName
        self.riders = []
        self.drivers = []
        self.rides = []

    def addRider(self, rider):
        self.riders.append(rider)

    def addDriver(self, driver):
        self.drivers.append(driver)

    def __repr__(self):
        return f'Welcome to {self.companyName} Application with {len(self.riders)} riders and {len(self.drivers)} drivers'


class User:
    def __init__(self, name, email, nationalId):
        self.name = name
        self.email = email
        self.nationalId = nationalId
        self.wallet = 0

    def displayProfile(self):
        print(f'UserName: {self.name}, UserEmail: {self.email}')


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
                        f'Ride requested by {self.name} to {destination} with driver {driver.name}')
                    break
            else:
                print("No available drivers at the moment.")


class Driver(User):
    def __init__(self, name, email, nationalId):
        super().__init__(name, email, nationalId)
        self.currentRide = None

    def isAvailable(self):
        return self.currentRide is None


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
        print(f'Ride from {self.startLocation} to {self.destination} ended.')


# Running the application
pyRide = RideSharing("PyRide")

# Create riders and drivers
rider1 = Rider("Rahman", "rahman@gmail.com", 222, 100)
rider1.currentLocation = "Dhanmondi"
driver1 = Driver("Sourav", "saurab@gmail.com", 64)

# Add users to the application
pyRide.addRider(rider1)
pyRide.addDriver(driver1)

# Rider requests a ride
rider1.requestRide(pyRide, "Uttara")

# End the ride
if rider1.currentRide:
    rider1.currentRide.endRide()

print(pyRide)
