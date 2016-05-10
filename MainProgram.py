from promptInput import inputPrompts
from UserInputFile import csvFileInputOutput
from AircraftFinder import AircraftFinder
from AirportAtlas import AirportAtlas
from CurrencyCodes import CurrencyDict
from ExchangeRates import ExchangeRates

# Main driver program which asks user for options of file-reading or manual input
def main():
    airportFinder = AirportAtlas("airport.csv")  # Initialise airport atlas to create a dictionary of airports
    currencyFinder = CurrencyDict("countrycurrency.csv")  # Create a dictionary of currencies
    exchangeFinder = ExchangeRates("currencyrates.csv")  # Create a dictionary of exchange rates
    aircraftFinder = AircraftFinder("aircraft.csv")  # Create a dictionary of aircraft

    print("Initialising program to calculate most economic route between a list of airports...\n")

    print("There are two input options available:\n"
          "(1) Read routes and aircraft from a file\n"
          "(2) Type in route and aircraft through command line\n")

    # Ask user to choose an option for input
    inputOption = input("Please enter input option (1 = file-reading, 2 = command line input): ")
    while inputOption != "1" and inputOption != "2":    # Make sure user enters 1 or 2
        inputOption = input("Error: please enter 1 or 2: ")

    if inputOption == "1":
        csvFileInputOutput(airportFinder, currencyFinder, exchangeFinder, aircraftFinder)
    else:
        inputPrompts(airportFinder, currencyFinder, exchangeFinder, aircraftFinder)


main()