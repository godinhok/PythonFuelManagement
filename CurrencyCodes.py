import os, csv  # import os and csv modules for csv reader
from Currency import Currency   # Import Currency class

class CurrencyDict:
    """Class to hold a dictionary of countries and their currency codes"""
    def __init__(self, filename = "countrycurrency.csv"):
        self.currencies = self.loadCurrencies(filename) # Dictionary of Currency objects

    # Method to load currencies into dictionary from a csv file
    def loadCurrencies(self, filename):
        # Check that input file has csv format
        if not filename.endswith(".csv"):
            print("Error: file {} is not a .csv file".format(filename))
            return {}
        # Open file
        try:
            with open(os.path.join(filename), "rt", encoding="UTF-8") as file:
                currencyReader = csv.reader(file)
                currencies = {}
                next(currencyReader, None)  # Skips the header row
                # Read in rows from csv file to create dictionary of currencies keyed by country
                for row in currencyReader:
                    currencies[row[0]]= Currency(row[0], row[17], row[14])
            return currencies
        except FileNotFoundError:
            print("Error: csv file {} not found".format(filename))
            return {}
        except IndexError:
            print("Error reading file {} - please check format".format(filename))
            return {}

    # Method to return a Currency object given a country name
    def getCurrency(self, country):
        try:
            return self.currencies[country] # Look up Currency object in dictionary
        except (KeyError, TypeError):
            print("Error: invalid country: {}" .format(country))
            return 0


