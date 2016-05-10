import os, csv  # import os and csv modules for csv reader

class ExchangeRates:
    """Class to hold a dictionary of exchange rates"""
    def __init__(self, filename = "currencyrates.csv"):
        self.rates = self.loadRates(filename)   # Dictionary of Rate objects

    # Method to create a dictionary of Rate objects from a csv file
    def loadRates(self, filename):
        # Check that input file has csv format
        if not filename.endswith(".csv"):
            print("Error: file {} is not a .csv file".format(filename))
            return {}
        # Open file
        try:
            with open(os.path.join(filename), "rt", encoding="UTF-8") as file:
                rateReader = csv.reader(file)
                rates = {}
                # Read in rows from csv file to create dictionary of exchange rate keyed by currency code
                for row in rateReader:
                    rates[row[1]]= Rate(row[1], float(row[2]), float(row[3]))
            return rates
        except FileNotFoundError:
            print("Error: csv file {} not found".format(filename))
            return {}
        except (IndexError, ValueError):
            print("Error reading file {} - please check format".format(filename))
            return {}

    # Method to return a Rate object given a currency code
    def getRate(self, code):
        try:
            return self.rates[code] # Look up Rate object in dictionary
        except (KeyError, TypeError):
            print("Error: invalid currency code: %s" %(code))
            return 0

    # Method to take an amount in local currency and convert it to euros
    def convertToEuro(self, local_value, code):
        rate = self.getRate(code)
        if rate == 0:
            return 0
        else:
            try:
                return local_value * rate.toEuro
            except (TypeError, ValueError):
                print("Error: Amount to convert {} is not a numeric value".format(local_value))
                return 0

    # Method to take an amount in euros and convert to local currency
    def convertFromEuro(self, euro_value, code):
        rate = self.getRate(code)
        if rate == 0:
            return 0
        else:
            try:
                return euro_value * rate.fromEuro
            except (TypeError, ValueError):
                print("Error: Amount to convert {} is not a numeric value".format(euro_value))
                return 0

class Rate:
    """Class to hold the exchange rate for a particular currency"""
    def __init__(self, code, toEuro, fromEuro):
        self.code = code    # Currency code
        self.toEuro = toEuro      # To Euro exchange rate
        self.fromEuro = fromEuro    # From Euro exchange rate

    # Method to define a string for a particular currency
    def __str__(self):
        return "1 EUR = {} {}; 1 {} = {} EUR"\
            .format(self.toEuro, self.code, self.code, self.fromEuro)

