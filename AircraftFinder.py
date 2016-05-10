import os, csv  # import os and csv modules for csv reader
from Aircraft import Aircraft

class AircraftFinder:
    """Class to build a dictionary of Aircraft objects"""
    def __init__(self, filename = "aircraft.csv"):
        self.aircraftDict = self.loadAircraft(filename) # Dictionary of Aircraft objects

    # Method to load a set of Aircraft objects from a csv file
    def loadAircraft(self, filename):
        # Check that input file has csv format
        if not filename.endswith(".csv"):
            print("Error: file {} is not a .csv file".format(filename))
            return {}
        # Open file
        try:
            with open(os.path.join(filename), "rt", encoding="UTF-8") as file:
                aircraftReader = csv.reader(file)
                next(aircraftReader, None)  # Skips the header row
                aircraftDict = {}
                # Read in rows from csv file to create dictionary of aircraft keyed by code
                for row in aircraftReader:
                    aircraftDict[row[0]]= Aircraft(row[0], row[2], row[3], int(row[4]))
            return aircraftDict
        except FileNotFoundError:
            print("Error: CSV file %s not found" %(filename))
            return {}
        except (ValueError, IndexError):
            print("Error reading file {} - please check format".format(filename))
            return {}

    # Method to return aircraft object given an aircraft code
    def getAircraft(self, code):
        try:
            return self.aircraftDict[code]  # Look up Aircraft object in dictionary
        except KeyError:
            print("Error: aircraft %s does not exist" %(code))
            return 0

    # Method to find aircraft with range greater than a given distance
    def getAircraftRange(self, distance):
        try:
            longRangeAircraft = []  # List to hold aircraft codes
            for aircraft in self.aircraftDict.values():
                if aircraft.range > distance:
                    longRangeAircraft.append(aircraft.planeType)    # List the aircraft with a range greater than input distance
            return longRangeAircraft
        except TypeError:   # Raise exception if distance is not given as a numeric value
            print("Error: Distance {} is not a numeric value".format(distance))
            return []