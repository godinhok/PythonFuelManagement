from AirportAtlas import AirportAtlas
from AircraftFinder import AircraftFinder
from ExchangeRates import *
from CurrencyCodes import CurrencyDict
from itertools import permutations

class Itinerary:
    """Class to hold a route between 5 airports and calculate the most economic route between them"""
    def __init__(self, route, aircraftCode, revisitCode = "", aircraftFinder=AircraftFinder(),
                 airportAtlas=AirportAtlas(), currencyDict=CurrencyDict(), exchangeRates=ExchangeRates()):
        self.airportAtlas = airportAtlas
        self.aircraftFinder = aircraftFinder
        self.currencyDict = currencyDict
        self.exchangeRates = exchangeRates
        self.error = [] # Attribute to hold error messages for invalid airport, aircraft and route
        self.route = route  # Holds a list containing a route between airports e.g. ["DUB", "AAL", "CDG", "JFK", "LHR", "DUB"]
        self.setAircraft(aircraftCode)  # Set up an aircraft object using the aircraft code given
        self.revisitCode = self.validateRevisit(revisitCode)  # Code for airport to revisit. Empty string "" indicates no revisits
        self.setBestRoutes()  # Get the cheapest price and routes

    # Method to define string to print for object
    def __str__(self):
        return "Route: {}; Aircraft: {}" \
               .format(self.route, self.aircraft)

    # Method to set up an aircraft object given its code
    def setAircraft(self, code):
        self.aircraft = self.aircraftFinder.getAircraft(code)
        if self.aircraft == 0:
            print("Setting aircraft to default type 747")
            self.error.append("Error: Invalid aircraft {} changed to 747".format(code))
            self.aircraft = self.aircraftFinder.getAircraft("747")

    def validateRevisit(self, code):
        if code == self.route[0]:
            print("Error: cannot revisit home airport {}. No revisits checked.".format(code))
            self.error.append("Error: cannot revisit home airport {}. No revisits checked.".format(code))
            return ""
        elif code in self.route or code == "":
            return code
        else:
            print("Error: revisit airport {} not in route list. No revisits checked.".format(code))
            self.error.append("Error: revisit airport {} not in route list. No revisits checked.".format(code))
            return ""

    # Method to calculate all permutations of routes to travel between list of airports
    def getRoutePermutations(self):
        home = self.route[0]    # Set home airport to first airport in route
        destinations = self.route[1:]  # Get a sublist of the airports that are not the home airport

        # If airport to revisit is specified
        if self.revisitCode != "":
            destinations.append(self.revisitCode)   # Append airport to revisit

        routePermutations = list(set(permutations(destinations)))    # Determine all permutations for route - use "set" to exclude duplicates
        for i in range(len(routePermutations)):
            routePermutations[i] = list(routePermutations[i]) # Convert tuples to list
            routePermutations[i].insert(0, home)   # Add home airport to start of each permutation
            routePermutations[i].insert(len(routePermutations[i]), home)  # Add home airport to end of each permutation

        # Remove cases where revisit airport appears beside itself in routePermutations list
        if self.revisitCode != "":
            for i in range(len(routePermutations)):
                for j in range(len(routePermutations[i])-1):
                    if routePermutations[i][j] == routePermutations[i][j+1]:    # Check for the same airport beside itself in the list
                        routePermutations[i] = "invalid"  # Set list value to invalid route
            # Remove invalid routes from revisit list
            while "invalid" in routePermutations:
                routePermutations.remove("invalid")

        return routePermutations

    # Function to check that airports in a particular route are valid
    def validateAirports(self):
        isValid = True  # Boolean to track if route is valid
        for i in range(len(self.route)):
            # Check for invalid airport codes in route
            if self.airportAtlas.getAirport(self.route[i]) == 0:
                self.error.append("Error: airport code {} is invalid".format(self.route[i]))   # Add invalid airports to error list
                isValid = False # set Boolean to false
        for airport in set(self.route):
            # Check for airports that appear more than once in route
            if self.route.count(airport) > 1:
                print("Error: Duplicate airport found in route: {}".format(airport))
                self.error.append("Error: Airport {} duplicated in route".format(airport)) # Add duplicate airports to error list
                isValid = False
            if isValid == False:
                self.bestPrice = -1 # Value of -1 indicates route cannot be calculated
        return isValid


    # Method to set the best route and price
    def setBestRoutes(self):
        # Initialise attributes for best route and price
        self.bestRoutes = []
        self.bestPrice = 0
        # Check for valid airport codes and duplicate airports in route list
        if self.validateAirports():
            self.otherAircraft = []  # List to hold other aircraft which may be able to fly route
            self.bestPrice, self.bestRoutes = self.getBestRoutes()

    # Method to calculate to calculate the most economic price and route
    def getBestRoutes(self):
        routePermutations = self.getRoutePermutations() # Get a list of permutations
        priceList = []
        for path in routePermutations:
            price = self.checkRoutePrice(path)   # Get the price of the path
            priceList.append(price) # Add the price to the price list

        # Get the minimum price in the list where it is not zero
        nonZeroPrices = [price for price in priceList if price > 0]

        if len(nonZeroPrices) == 0: # Check for lists where there are no valid routes
            return 0, []    # If there are no valid routes, return empty bestPrice and bestRoutes

        bestPrice = min(nonZeroPrices)      # Get the minimum price

        # Create a list of the cheapest routes
        bestRoutes = []
        for i in range(len(priceList)):
            if priceList[i] == bestPrice:
                bestRoutes.append(routePermutations[i])
        return bestPrice, bestRoutes

    # Method to check the price of a route given a path between airports
    def checkRoutePrice(self, path):
        self.aircraft.addFuel(self.aircraft.maxFuel)    # Fuel aircraft to maximum at start of journey
        # Calculate cost for initial fuelling of aircraft at home airport
        totalFuelCost = self.getFuelPrice(self.aircraft.maxFuel, path[0])

        totalDist = 0   # holds the distance travelled without refuelling
        for i in range(len(path) - 1):
            # Calculate distance between two airports
            distance = self.airportAtlas.calcAirportDist(path[i], path[i+1])

            if distance > self.aircraft.range:  # Check if distance is within range of aircraft
                # Find other aircraft with range greater than the distance given
                longRangeAircraft = self.aircraftFinder.getAircraftRange(distance)
                for aircraft in longRangeAircraft:
                    if aircraft not in self.otherAircraft:
                        self.otherAircraft.append(aircraft) # Add longer range aircraft to list
                #print("Cannot fly between {} and {} - distance ({}km) is greater than aircraft range ({}km)"
                #      .format(path[i], path[i+1], round(distance, 2), self.aircraft.range))
                return 0
            else:
                totalDist += distance   # Calculate the total distance travelled

                # Check if total distance travelled is above aircraft range or if aircraft does not have enough fuel
                if (totalDist > self.aircraft.range) or (self.aircraft.getFuel() < self.aircraft.MIN_FUEL):
                    # Calculate the volume of fuel needed to fill the aircraft
                    fuelVolume = self.aircraft.maxFuel - self.aircraft.getFuel()
                    self.aircraft.addFuel(fuelVolume)   # Refuel aircraft
                    # Calculate the cost of refuelling
                    totalFuelCost += self.getFuelPrice(fuelVolume, path[i])
                    totalDist = distance   # set total distance travelled to distance for this leg

                self.aircraft.useFuel(distance) # Aircraft is assumed to consume 1 litre per kilometre


        return totalFuelCost    # Return the total fuel cost for the route

    # Method to determine the price of fuel given the amount of fuel and the airport code
    def getFuelPrice(self, fuelAmount, airportCode):
        country = self.airportAtlas.getAirport(airportCode).country    # Look up the airport country
        currencyCode = self.currencyDict.getCurrency(country).code  # Look up the currency code
        toEuroRate = self.exchangeRates.getRate(currencyCode).toEuro    # Get the To Euro exchange rate
        return toEuroRate * fuelAmount  # Calculate the price of fuel by multiplying the to Euro rate



