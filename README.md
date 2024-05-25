# PyRide - A Simplified RideSharing Application

## Overview

PyRide is a Python-based ride-sharing application built using Object-Oriented Programming (OOP) concepts. This project was developed as part of the university course **Object Oriented Programming II Lab (CSE 222)**. The application allows users to register as either riders or drivers, request rides, and manage ride operations.

## Core Features

- **Ride Sharing Platform:** Manage and facilitate rides between riders and drivers.
- **User Profiles:** Separate classes for riders and drivers with profile management.
- **Ride Management:** Request and manage rides, including starting and ending rides.
- **Wallet System:** Riders have a wallet to manage their ride payments.

## Classes and Their Responsibilities

### 1. `RideSharing`
This class is the main application class managing riders, drivers, and rides.

- **Attributes:**
  - `companyName`: Name of the ride-sharing company.
  - `riders`: List of registered riders.
  - `drivers`: List of registered drivers.
  - `rides`: List of ongoing and completed rides.

- **Methods:**
  - `__init__(self, companyName)`: Initializes the ride-sharing application with a company name.
  - `addRider(self, rider)`: Adds a rider to the riders list.
  - `addDriver(self, driver)`: Adds a driver to the drivers list.
  - `__repr__(self)`: Returns a string representation of the company, including the number of riders and drivers.

### 2. `User`
This class is a base class for both riders and drivers.

- **Attributes:**
  - `name`: User's name.
  - `email`: User's email.
  - `nationalId`: User's national ID.
  - `wallet`: User's wallet balance.

- **Methods:**
  - `__init__(self, name, email, nationalId)`: Initializes a user with name, email, and national ID.
  - `displayProfile(self)`: Prints the user's profile information.

### 3. `Rider` (Inherits from `User`)
This class represents a rider in the ride-sharing application.

- **Attributes:**
  - `name`, `email`, `nationalId`, `wallet` (inherited from `User`)
  - `currentRide`: The current ride the rider is engaged in.
  - `currentLocation`: The current location of the rider.

- **Methods:**
  - `__init__(self, name, email, nationalId, initialAmount)`: Initializes a rider with an initial wallet amount.
  - `requestRide(self, rideSharing, destination)`: Allows the rider to request a ride to a destination.

### 4. `Driver` (Inherits from `User`)
This class represents a driver in the ride-sharing application.

- **Attributes:**
  - `name`, `email`, `nationalId`, `wallet` (inherited from `User`)
  - `currentRide`: The current ride the driver is engaged in.

- **Methods:**
  - `__init__(self, name, email, nationalId)`: Initializes a driver.
  - `isAvailable(self)`: Checks if the driver is available for a new ride.

### 5. `Ride`
This class represents a ride between a rider and a driver.

- **Attributes:**
  - `rider`: The rider requesting the ride.
  - `driver`: The driver accepting the ride.
  - `startLocation`: The starting location of the ride.
  - `destination`: The destination of the ride.
  - `startTime`: The time when the ride started.
  - `endTime`: The time when the ride ended (set during ride completion).

- **Methods:**
  - `__init__(self, rider, driver, destination)`: Initializes a ride with the rider, driver, and destination.
  - `endRide(self)`: Ends the ride and resets the current ride status for both rider and driver.
