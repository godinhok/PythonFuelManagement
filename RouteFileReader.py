from Itinerary import Itinerary
from AircraftFinder import AircraftFinder
from AirportAtlas import AirportAtlas
from CurrencyCodes import CurrencyDict
from ExchangeRates import ExchangeRates
import csv, os

class ItineraryFinder:
    """Class to create a list of itineraries from a file and print a list of best routes to another file"""
    # Constructor for class - takes a filename as input and populates a list of Itinerary objects
    def __init__(self, filename = "testroutes.csv", aircraftFinder=AircraftFinder(),
                 airportAtlas=AirportAtlas(), currencyDict=CurrencyDict(), exchangeRates=ExchangeRates()):
        # List of Itinerary objects
        self.itineraries = self.loadData(filename, aircraftFinder, airportAtlas, currencyDict, exchangeRates)

    # Method to load data from csv file into a dictionary of Itinerary objects
    def loadData(self, csvFile, aircraftFinder, airportAtlas, currencyDict, exchangeRates):
        # Open file
        try:
            with open(os.path.join(csvFile), "rt", encoding="UTF-8") as file:
                routeReader = csv.reader(file)
                itineraries = []
                next(routeReader, None)  # Skips the header row
                # Read in rows from csv file to create dictionary of itineraries
                i = 0
                for row in routeReader:
                    print("Reading in Route {}...".format(i+1))
                    itineraries.append(Itinerary(row[0:5], row[5], row[6], aircraftFinder,
                                                 airportAtlas, currencyDict, exchangeRates))    # Create a list of Itinerary objects
                    print("Route {}: {}".format(i+1, itineraries[i]))
                    i += 1
            return itineraries
        except FileNotFoundError:
            print("Error: CSV file {} not found.".format(csvFile))
            return 0
        except IndexError:
           print("Error: cannot read CSV file - please check format.")
           return 0

    # Method to write out best routes to a file
    def outputBestRoutes(self, outputFile="bestroutes.csv"):
        try:
            # Open file
            with open(os.path.join(outputFile), "w", newline='') as file:
                routeWriter = csv.writer(file, delimiter=",")
                # Iterate through list of Itinerary objects
                for i in range(len(self.itineraries)):
                    print("Getting most economic routes for Route {}...".format(i+1))
                    # Write the route number to file
                    csvrow = ["Route {}".format(i+1)]
                    routeWriter.writerow(csvrow)
                    # If there are valid routes
                    if self.itineraries[i].bestPrice > 0:
                        csvrow = []
                        csvrow += "", "Fuel price", "€"+str(self.itineraries[i].bestPrice)
                        routeWriter.writerow(csvrow)    # Write fuel price to file
                    # Write aircraft type to file
                    csvrow = ["", "Aircraft", self.itineraries[i].aircraft.planeType]
                    routeWriter.writerow(csvrow)

                    # If no routes could be calculated due to incorrect input
                    if self.itineraries[i].bestPrice == -1:
                        routeWriter.writerow(["", "Invalid input: no routes calculated"])

                    # If there are no valid itineraries
                    elif len(self.itineraries[i].bestRoutes) == 0:
                        routeWriter.writerow(["", "No routes found within aircraft range"])
                        # Write other aircraft options to file if they are available
                        if len(self.itineraries[i].otherAircraft) > 0:
                            csvrow = ["", "Suggested aircraft"]
                            for aircraft in self.itineraries[i].otherAircraft:
                                csvrow.append(aircraft)
                            routeWriter.writerow(csvrow)

                    else:   # If there are routes within the range of the aircraft
                        for route in self.itineraries[i].bestRoutes:    # For each route in the list of best routes
                            csvrow = [""] # Holds a list to write to a row of the CSV file
                            for j in range(len(route)):
                                csvrow.append(route[j]) # Append the airport code to the row
                            routeWriter.writerow(csvrow)    # Write the route row to the file

                    # Write error messages about routes and aircraft
                    if len(self.itineraries[i].error) > 0:
                        for error in self.itineraries[i].error:
                            routeWriter.writerow(["", error])

                    routeWriter.writerow([])  # Write a blank row to separate routes

            print("\nOutput file {} created successfully".format(outputFile))

        except PermissionError:
            print("Error: Cannot create output file {} - please close file or choose another filename".format(outputFile))
            filename = input("Please confirm your output file name: ")
            self.outputBestRoutes(filename)

