import unittest
from AircraftFinder import AircraftFinder

class testAircraftFinderClass(unittest.TestCase):
    """Unit tests for AirportFinder class"""
    def setUp(self):
        self.testAircraftFinder = AircraftFinder("aircraft.csv")

    # Test to check if valid csv file can be loaded
    def testValidCsvFile(self):
        self.assertEqual(len(self.testAircraftFinder.aircraftDict), 16)

    # Test to check if non-csv file can be loaded
    def testNonCsvFile(self):
        myAircraftFinder = AircraftFinder("AirportAtlas.py")
        self.assertEqual(myAircraftFinder.aircraftDict, {})

    # Test to check if csv file that does not exist can be loaded
    def testNonExistentCsvFile(self):
        myAircraftFinder = AircraftFinder("air.csv")
        self.assertEqual(myAircraftFinder.aircraftDict, {})

    # Test to check if invalid csv file can be loaded
    def testInvalidCsvFile(self):
        myAircraftFinder = AircraftFinder("airport.csv")
        self.assertEqual(myAircraftFinder.aircraftDict, {})
        myAircraftFinder = AircraftFinder("testroutes.csv")
        self.assertEqual(myAircraftFinder.aircraftDict, {})
        myAircraftFinder = AircraftFinder("currencyrates.csv")
        self.assertEqual(myAircraftFinder.aircraftDict, {})

    # Test to check look up of valid aircraft codes
    def testValidAircraft(self):
        aircraft = self.testAircraftFinder.getAircraft("747")
        self.assertEqual(str(aircraft), "Boeing 747")
        aircraft = self.testAircraftFinder.getAircraft("C212")
        self.assertEqual(str(aircraft), "Airbus C212")
        aircraft = self.testAircraftFinder.getAircraft("DC8")
        self.assertEqual(str(aircraft), "Douglas DC8")

    # Test to check look up of invalid aircraft codes
    def testInValidAircraft(self):
        aircraft = self.testAircraftFinder.getAircraft("abc")
        self.assertEqual(aircraft, 0)
        aircraft = self.testAircraftFinder.getAircraft(123)
        self.assertEqual(aircraft, 0)

    # Test to get list of aircraft with range greater than particular value
    def testGetAircraftRange(self):
        aircraftList = self.testAircraftFinder.getAircraftRange(15000)
        for aircraft in ['MD11', '777', '747']:
            self.assertTrue(aircraft in aircraftList)
        aircraftList = self.testAircraftFinder.getAircraftRange(20000)
        self.assertEqual(aircraftList, ['MD11'])

    # Test to get list of aircraft with range greater than particular value if invalid distance type given
    def testGetRangeWithInvalidDistance(self):
        aircraftList = self.testAircraftFinder.getAircraftRange("abc")  # Test distance as string
        self.assertEqual(aircraftList, [])
        aircraftList = self.testAircraftFinder.getAircraftRange([12,24])    # Test distance as list
        self.assertEqual(aircraftList, [])

if __name__ == '__main__':
    unittest.main()
