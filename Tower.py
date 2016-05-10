from Aircraft import Aircraft

# Class tower to hold information about airport tower
class Tower:
    """Class for airport tower"""
    def __init__(self):
        self.flightList = []    # Attribute flight list holds a list of flights from the airport
#        print("New tower created")

    def updateFlightList(self, flightList):
        for item in flightList:
            if type(item) == str:
                self.flightList.append(item)
            else:
                print("Error:", item, "is not a valid flight number")

#    5. Add a method requestFlightClearance(anAirplane) to the Tower class that takes an Aircraft
#object checks its flight number against its list of flights and gives clearance to take off it the
#flight is in the list.
    # Method to request flight clearance for an aircraft
    def requestFlightClearance(self, anAircraft):
        if anAircraft.flightNumber in self.flightList:
            print("Aircraft cleared for takeoff.")
            anAircraft.setFlightClearance(True)
        else:
            print("Flight number does not appear in flight list. Flight not cleared for takeoff.")
            anAircraft.setFlightClearance(False)
