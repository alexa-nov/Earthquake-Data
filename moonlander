def showWelcome():
    print("Welcome aboard the Lunar Module Flight Simulator")
    print("\nTo begin you must specify the LM's initial altitude")
    print("and fuel level.  To simulate the actual LM use")
    print("values of 1300 meters and 500 liters, respectively.")
    print("\nGood luck and may the force be with you!")

def getFuel():
    fuel = int(input("\nEnter the initial amount of fuel on board the LM (in liters): "))
    while fuel <= 0:
        print("ERROR: Amount of fuel must be positive, please try again")
        fuel = int(input("Enter the intital amount of fuel on board the LM (in liters): "))
    return fuel

def getAltitude():
    altitude = int(input("Enter the initial altitude of the LM (in meters): "))
    while altitude < 1 or altitude > 9999:
        print("ERROR: Altitude must be between 1 and 9999, inclusive, please try again") 
        altitude = int(input("Enter the initial altitude of the LM (in liters): "))
    return altitude

def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    #print("\nLM state at retrorocket cutoff")
    #if fuelAmount <= 0:
        #print("\nLM state at landing/impact")
    if fuelAmount > 0:
        print("%13s %4d s" %("Elapsed Time:", elapsedTime))
        print("%13s %4d l" %("Fuel:", fuelAmount))
        print("%13s %4d l/s" %("Rate:", fuelRate))
        print("%13s %7.2f m" %("Altitude:", altitude))
        print("%13s %7.2f m/s" %("Velocity:", velocity))

def getFuelRate(currentFuel):
    rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    if rate < currentFuel:
        while rate < 0 or rate > 9:
            print("ERROR: Fuel rate must be between 0 and 9, inclusive")
            rate = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    return rate
    else:
        return currentFuel   
   
def updateAcceleration(gravity, fuelRate):
    return gravity * (fuelRate / 5 - 1)
	
def updateAltitude(altitude, velocity, acceleration):
    updateAlt = altitude + velocity + acceleration / 2
    if updateAlt >= 0:
        return updateAlt

def updateVelocity(velocity, acceleration):
    return velocity + acceleration

def updateFuel(fuel, fuelRate):
    return fuel - fuelRate

def displayLMLandingStatus(velocity):
    if velocity <= 0 and velocity >= -1:
        print("Status at landing - The eagle has landed!")
    if velocity <= -1 and velocity >= -10:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    if velocity <= -10:
        print("Status at landing - Ouch - that hurt!") 
