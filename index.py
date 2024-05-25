from ride_sharing import RideSharing
from rider import Rider
from driver import Driver

# Running the application
pyRide = RideSharing("PyRide")

# Print the welcome message first
print(pyRide)

# Create riders and drivers
rider1 = Rider("Rakib", "rahman@gmail.com", 222, 100)
rider1.currentLocation = "Mirpur-01"
driver1 = Driver("Sourav", "saurab@gmail.com", 64)

# Add users to the application
pyRide.addRider(rider1)
pyRide.addDriver(driver1)

# Rider requests a ride
rider1.requestRide(pyRide, "Uttara")

# End the ride
if rider1.currentRide:
    rider1.currentRide.endRide()

# Print the final conclusion message
print("Thanks for being with US 😃")
