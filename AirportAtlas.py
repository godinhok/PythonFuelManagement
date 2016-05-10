import os, csv  # import os and csv modules for csv reader
from Airport import Airport  # import Airport class
from math import pi, sin, cos, acos  # import math functions for distance calculator


class AirportAtlas:
    """Class to load a dictionary of airports from a csv file"""
    # Constructor for airport atlas. Takes a filename as input and populates a dictionary of Airport objects
    def __init__(self, filename="airport.csv"):
        self.airports = self.loadData(filename) # Dictionary of Airport objects

    # Method to load data from csv file into a dictionary of Airport objects
    def loadData(self, csvFile):
        # Check that input file has csv format
        if not csvFile.endswith(".csv"):
            print("Error: file {} is not a .csv file".format(csvFile))
            return 0
        # Open file
        try:
            with open(os.path.join(csvFile), "rt", encoding="UTF-8") as file:
                airportReader = csv.reader(file)
                airportDict = {}
                # Read in rows from csv file to create dictionary of airports keyed by airport code
                for row in airportReader:
                    airportDict[row[4]] = Airport(row[4], row[1], row[2], row[3], row[6], row[7])
            return airportDict
        except FileNotFoundError:
            print("Error: CSV file %s not found" % (csvFile))
            return 0
        except (ValueError, IndexError):
            print("Error reading file {} - please check format".format(csvFile))
            return 0

    # Method to return an Airport object given an airport code
    def getAirport(self, code):
        try:
            return self.airports[code]  # Look up airport code in dictionary
        except KeyError:
            print("Error: airport code %s is invalid" %(code))
            return 0

    # Static method to calculate great circle distance
    @staticmethod
    def greatcircledist(lat1, long1, lat2, long2):
        # Calculate angle to pole
        poleAng1 = 90 - lat1
        poleAng2 = 90 - lat2

        # Convert angles to radians
        poleAng1 = poleAng1 * 2 * pi / 360
        poleAng2 = poleAng2 * 2 * pi / 360
        long1 = long1 * 2 * pi / 360
        long2 = long2 * 2 * pi / 360

        radiusEarth = 6371  # earth's radius is approx 6371 km

        # return distance between 2 points using formula
        return acos(sin(poleAng1) * sin(poleAng2) * cos(long1 - long2) + cos(poleAng1) * cos(poleAng2)) * radiusEarth

    # Method to calculate the distance between two airports given the airport codes
    def calcAirportDist(self, code1, code2):
        airport1 = self.getAirport(code1)
        airport2 = self.getAirport(code2)
        # Check for invalid airport codes
        if airport1 == 0 or airport2 == 0:
            return 0
        return self.greatcircledist(airport1.latitude, airport1.longitude, airport2.latitude, airport2.longitude)

