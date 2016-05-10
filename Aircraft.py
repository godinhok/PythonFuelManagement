# Class to define an aeroplane object
class Aircraft:
    """Class to define an aircraft object"""
    # initialise object with default plane type 747
    def __init__(self, planeType = "747", units = "imperial", manufacturer = "Boeing", range = 9800):
        self.manufacturer = manufacturer
        self.planeType = planeType  # sets type of aircraft e.g. 747, 737, etc.
        self.range = self.calcRange(units, range)  # stores range of aircraft in km
        self.__fuel = 0 # private attribute containing current aircraft fuel
        self.maxFuel = self.range    # Sets maximum fuel capacity of aircraft - assuming aircraft burns 1 litre per km
        self.__fuelCheck = False    # Boolean flag to check fuel amount, false if not enough fuel for takeoff
        self.MIN_FUEL = 1000    # minimum amount of fuel for takeoff
        self.flightNumber = ""
        self.__flightClearance = False

    # Method to define string for the Aircraft object
    def __str__(self):
        return "{} {}" \
               .format(self.manufacturer, self.planeType)

    # Method to calculate range of aircraft in km
    def calcRange(self, units, range):
        if type(range) == int or type(range) == float:
            if units == "metric":
                return range
            elif units == "imperial":    # Convert imperial units to kilometres
                return range * 1.609 # 1 mile = 1.609 km
            else:
                print("Error:", units, "not a valid unit for range - setting to metric units.")
                return range
        else:
            print("Error: range should be a numeric value")
            return 0

    # Method to check if current fuel level is above/below minimum amount
    def fuelCheck(self):
        if self.__fuel < self.MIN_FUEL: # Check if fuel is below minimum amount
            print("Fuel check failed: Current fuel is below safe limit. Current fuel is: {} L, below limit of: {} L"
                  .format(self.__fuel, self.MIN_FUEL))
            self.__fuelCheck = False    # set Boolean flag to false
        else:   # If fuel is above minimum value
            print("Fuel check complete. Current fuel level is: {} L".format(self.__fuel))
            self.__fuelCheck = True # set Boolean flag to true

    # Method to clear plane for takeoff
    def takeOff(self):
        if self.__fuelCheck == True:    # If Boolean flag indicates fuel above safe limit
            print("Cleared for Takeoff! Fasten your seat-belt!")
        else:
            print("Takeoff failed: please complete pre-flight check.")
            print(self.fuelCheck()) # Carry out fuel check

    # method to print current fuel in aircraft
    def printStatus(self):
        print("Current fuel: {} L".format(self.__fuel))

    # Method to add fuel to aircraft
    def addFuel(self, volume):
        unusedFuel = 0
        try:
            if volume < 0:  # if volume of fuel is below 0, cannot remove fuel
                print("No syphoning fuel!")
            elif self.__fuel + volume <= self.maxFuel:  # Add total volume if it remains below maximum fuel capacity
                self.__fuel = self.__fuel + volume
            elif self.__fuel + volume > self.maxFuel:   # If volume added is above fuel capacity of aircraft
                self.__fuel = self.maxFuel  # Refuel aircraft to maximum volume
                unusedFuel = volume - self.__fuel   # Calculate unused fuel
            return unusedFuel   # return the amount of unused fuel
        except TypeError:
            print("Error: volume is not a numeric value")

    # Method to check flight clearance of aircraft
    def preFlightCheck(self):
        print("Starting pre-flight checks")
        if self.__fuelCheck == True and self.__flightClearance == True:
            print("Pre-flight check complete!")
        elif self.__fuelCheck == False:
            print("Pre-flight check failed! Please complete fuel check.")
        else:
            print("Pre-flight check failed! Please complete flight clearance.")

    # Method to set flight clearance
    def setFlightClearance(self, clearance):
        self.__flightClearance = clearance

    # Method for aircraft to use fuel during flight
    def useFuel(self, amount):
        try:
            if amount > 0:
                self.__fuel -= amount
            else:
                print("Error: cannot use a negative amount of fuel")
        except TypeError:
            print("Error: amount of fuel is not a numeric value")

    # Method to get the remaining fuel in the aircraft
    def getFuel(self):
        return self.__fuel
