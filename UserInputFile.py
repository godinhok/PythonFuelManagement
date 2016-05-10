from RouteFileReader import ItineraryFinder

# Program to determine best routes given an input file containing a list of routes
def csvFileInputOutput(airportFinder, currencyFinder, exchangeFinder, aircraftFinder):
    # Ask user for input file name
    print("Please provide an input file containing your itinerary and aircraft.\n"
          "See testroutes.csv for correct file format.\n")
    userInput = input("Please enter your input csv file name: ")
    # Make sure file has csv format
    while not userInput.endswith(".csv"):
        print("\nError: input file should be in csv format.")
        userInput = input("Please enter input filename of type '.csv': ")

    print("Reading {}...\n".format(userInput))
    # Create Itinerary objects from input file using ItineraryFinder
    userItineraries = ItineraryFinder(userInput, aircraftFinder, airportFinder, currencyFinder, exchangeFinder)
    # Check for errors in input file
    while userItineraries.itineraries == 0: # Value of zero indicates error in reading csv file
        userInput = input("Please re-enter csv file name: ")
        userItineraries = ItineraryFinder(userInput)

    # Ask user for output file name
    userOutput = input("\nPlease enter your output csv file name: ")
    # Make sure output file differs from input filename
    while userOutput == userInput:
        print("\nError: output filename should differ from input file.")
        userOutput = input("Please enter a new output filename: ")
    # Make sure output file is of csv format
    while not userOutput.endswith(".csv"):
        print("\nError: output file should be in csv format.")
        userOutput = input("Please enter output filename ending with '.csv': ")

    # Create output file
    userItineraries.outputBestRoutes(userOutput)
    print("\nFinished finding economic routes. Please check your output in {} for details.".format(userOutput))

