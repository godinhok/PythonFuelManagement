import unittest
from AirportAtlas import AirportAtlas

class testAirportAtlas(unittest.TestCase):
    """Unit tests for Airport Atlas class"""
    def setUp(self):
        self.testAtlas = AirportAtlas("airport.csv")

    # Test to validate known airport distances
    def testGetDistBetweenKnownValues(self):
        self.known_values = (("DUB", "SYD", 17215), ("DUB", "AAL", 1096), ("DUB", "CDG", 784))

        for code_1, code_2, dist in self.known_values:

            result = int(self.testAtlas.calcAirportDist(code_1, code_2))

            self.assertEqual(dist, result)

    # Test to validate distance between same airport is zero
    def testDistanceBetweenDublinIsZero(self):
        code_1 = 'DUB'
        code_2 = 'DUB'
        dist = 0
        result = self.testAtlas.calcAirportDist(code_1, code_2)
        self.assertEqual(dist, result)

    # Test to check errors for invalid airport code
    def testInvalidAirportCode(self):
        result = self.testAtlas.getAirport("ABC")
        self.assertEqual(result, 0)

    # Test to check valid airport code
    def testValidAirportCode(self):
        result = self.testAtlas.getAirport("DUB")
        self.assertEqual(str(result), "DUB: Dublin Airport, Dublin, Ireland")

    # Test to check a list of valid airport codes
    def testValidAirportCodeList(self):
        testCodes = ["DUB", "KHT", "KAB", "MQI", "RMY"]
        for code in testCodes:
            self.assertTrue(self.testAtlas.getAirport(code))

    # Test to load airport dictionary using a valid csv file
    def testValidCsvFile(self):
        self.assertTrue(len(self.testAtlas.airports) > 0)

    # Test to load airport dictionary from a file that does not exist
    def testFileNotExist(self):
        testAtlas = AirportAtlas("air.csv")
        self.assertEqual(testAtlas.airports, 0)

    # Test to load airport dictionary from a non-csv file
    def testNonCsvFile(self):
        testAtlas = AirportAtlas("Currency.py")
        self.assertEqual(testAtlas.airports, 0)

    # Test to load airport dictionary from a csv file with incorrect format
    def testIncorrectFormatFile(self):
        testAtlas = AirportAtlas("aircraft.csv")
        self.assertEqual(testAtlas.airports, 0)
        testAtlas = AirportAtlas("testroutes.csv")
        self.assertEqual(testAtlas.airports, 0)
        testAtlas = AirportAtlas("currencyrates.csv")
        self.assertEqual(testAtlas.airports, 0)

    # Test to calculate distance between invalid airports
    def testInvalidAirportDist(self):
        self.assertEqual(self.testAtlas.calcAirportDist("DUB", "a"), 0)
        self.assertEqual(self.testAtlas.calcAirportDist("b", "a"), 0)

if __name__ == '__main__':
    unittest.main()
