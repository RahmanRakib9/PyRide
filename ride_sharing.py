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
