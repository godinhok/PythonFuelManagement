from AirportAtlas import AirportAtlas
from Itinerary import Itinerary
from ExchangeRates import ExchangeRates
from CurrencyCodes import CurrencyDict
from AircraftFinder import AircraftFinder


# Function to print the most economic routes for a given itinerary
def printBestRoutes(itinerary):
    print("\nSearching for the most economic route between airports {} using a {}...\n"
          .format(itinerary.route, itinerary.aircraft))
    if len(itinerary.bestRoutes) > 1:  # Print best routes if several routes at same price
        print("There are %d options with the same fuel price" % (len(itinerary.bestRoutes)))
        for i in range(len(itinerary.bestRoutes)):
            print("Option %d:" % (i + 1), itinerary.bestRoutes[i], "Fuel cost: €%d" % (itinerary.bestPrice))
    elif len(itinerary.bestRoutes) == 1:  # Print best route if only one cheapest route
        print("Most economic route is", itinerary.bestRoutes[0], "Fuel cost: €%d" % (itinerary.bestPrice))
    else:  # If there are no itineraries within the range of the aircraft
        selectOtherAircraft(itinerary)


# Function to change aircraft and print best routes
def selectOtherAircraft(itinerary):
    print("There are no routes within the range of the aircraft {}.\n"
          "Checking if alternative aircraft are available...".format(itinerary.aircraft))

    # If there are other aircraft that may have a suitable range for the route
    if len(itinerary.otherAircraft) > 0:
        # Print a list of suitable aircraft
        print("These aircraft may be suitable for your route: {}".format(itinerary.otherAircraft))
        tryOtherAircraft = input("Would you like to try the same route with a different aircraft? (Enter y/n): ")

        while tryOtherAircraft != "y" and tryOtherAircraft != "n":
            tryOtherAircraft = input("Error: please enter y or n: ")

        if tryOtherAircraft == "y":
            # Ask user to enter code for new aircraft
            newAircraft = input("Please enter the code for your new aircraft: ")
            # Check if new aircraft is in list of options
            while newAircraft not in itinerary.otherAircraft:
                newAircraft = input("Error: please enter an aircraft from the list {}".format(itinerary.otherAircraft))
            # Update the aircraft in the itinerary and find the most economic routes
            itinerary.setAircraft(newAircraft)
            itinerary.setBestRoutes()
            printBestRoutes(itinerary)
        else:  # If user does not want to try other aircraft
            print("Thank you. Please try again with alternate routes and aircraft.")
    else:
        print("There are no available aircraft with the range for your route. Please alter your route.")


# Main program to run to determine best routes given a set of five input airports
def inputPrompts(airportFinder, currencyFinder, exchangeFinder, aircraftFinder):
    # Ask user to enter airport codes for airports to visit
    userRoute = []  # Holds a list of airports to visit
    print("Please enter the airports you wish to visit.")

    # Ask user for their home airport
    while 1:
        home = input("Please enter your home airport: ")
        if airportFinder.getAirport(home) != 0:  # Check for valid airport code (invalid code returns 0)
            break
    userRoute.append(home)  # Add airport to route list

    # Ask user for the other airports they wish to visit
    for i in range(2, 6):

        while 1:
            airportCode = input("Please enter airport %s: " % (i))
            if airportCode not in userRoute:
                if airportFinder.getAirport(airportCode) != 0:  # Check for valid airport codes (invalid code returns 0)
                    break
            else:
                print("Error: %s already entered. Please enter a different airport code." % (airportCode))

        userRoute.append(airportCode)  # Add airport to route list

    # Ask user for aircraft type
    while 1:
        userAircraft = input("\nPlease enter the code of the aircraft you are using: ")
        if aircraftFinder.getAircraft(userAircraft) != 0:
            break

    # Ask user if they want to revisit airports
    revisit = input("\nDo you want to revisit one airport? (y/n) ")
    while 1:
        if revisit == "y" or revisit == "n":  # Check that user enters "y" or "n"
            break
        else:
            revisit = input("Please enter 'y' or 'n': ")

    # If user wants to revisit one airport ask for the code of the airport
    if revisit == "y":
        revisitCode = input("Please enter the code for the airport you want to revisit from your destinations {}: ".format(userRoute[1:]))
        while 1:
            if revisitCode not in userRoute:
                revisitCode = input("Error: invalid airport code. Please enter an airport code "
                                    "from the list {}: ".format(userRoute[1:]))
            elif revisitCode == userRoute[0]:
                revisitCode = input("Error: Cannot revisit home airport. Please enter a different airport "
                                    "from the list {}: ".format(userRoute[1:]))
            else:
                break
    else:
        revisitCode = ""

    # Create an Itinerary object for the chosen route
    userItinerary = Itinerary(userRoute, userAircraft, revisitCode, aircraftFinder, airportFinder, currencyFinder,
                              exchangeFinder)

    # Print out the most economic routes along with their prices
    printBestRoutes(userItinerary)

    # Ask if user wants to fly using the most economic route
    if len(userItinerary.bestRoutes) > 0:
        flyRoute = input("Do you want to fly your route ({})? (y/n) ".format(userItinerary.bestRoutes[0]))

        while 1:
            if flyRoute == "y" or flyRoute == "n":  # Check that user enters "y" or "n"
                break
            else:
                flyRoute = input("Please enter 'y' or 'n': ")

        if flyRoute == "n":
            print("Goodbye. We wish you a pleasant flight.")
        else:
            route = userItinerary.bestRoutes[0] # set route to first route in best routes list
            aircraft = userItinerary.aircraft
            # Start by fuelling aircraft to full capacity at start of journey
            print("Fuelling aircraft to full capacity at", route[0])
            aircraft.addFuel(aircraft.maxFuel)  # Fuel aircraft to maximum

            totalDist = 0  # holds the distance travelled without refuelling

            for i in range(len(route) - 1):
                print("\nPreparing your {} for takeoff from {}".format(aircraft, route[i]))
                aircraft.printStatus()

                # Calculate distance between two airports
                distance = airportFinder.calcAirportDist(route[i], route[i + 1])
                totalDist += distance  # Calculate the total distance travelled

                # Check if total distance travelled is above aircraft range or if aircraft does not have enough fuel
                if totalDist > aircraft.range or aircraft.getFuel() < aircraft.MIN_FUEL:
                    # Calculate the volume of fuel needed to fill the aircraft
                    fuelVolume = aircraft.maxFuel - aircraft.getFuel()
                    aircraft.addFuel(fuelVolume)  # Refuel aircraft
                    print("Refuelling aircraft in", route[i])
                    aircraft.printStatus()
                    totalDist = distance  # Reset total distance to zero

                aircraft.fuelCheck()    # Check that fuel level is ok to fly
                aircraft.takeOff()  # Takefo
                aircraft.useFuel(distance)  # Aircraft is assumed to consume 1 litre per kilometre
                print("\nFlew {} km and landed in {}".format(distance, route[i + 1]))
