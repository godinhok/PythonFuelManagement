import unittest
from Airport import Airport

class testAirportClass(unittest.TestCase):
    """Unit tests for Airport class"""
    def setUp(self):
        self.testAirport = Airport("TST", "TestAirport", "TestCity", "TestCountry", 12.345, 67.89)

    # Test to check airport attributes are correctly set up
    def testAirportSetup(self):
        self.assertEqual(self.testAirport.code, "TST")
        self.assertEqual(self.testAirport.name, "TestAirport")
        self.assertEqual(self.testAirport.city, "TestCity")
        self.assertEqual(self.testAirport.country, "TestCountry")
        self.assertEqual(self.testAirport.latitude, 12.345)
        self.assertEqual(self.testAirport.longitude, 67.89)

    # Test to check set up of airport with incorrect type for latitude/longitude
    def testLatLongType(self):
        myAirport = Airport("TST", "TestAirport", "TestCity", "TestCountry", "abc", 67.89)
        self.assertEqual(myAirport.latitude, 0)
        self.assertEqual(myAirport.longitude, 0)
        myAirport = Airport("TST", "TestAirport", "TestCity", "TestCountry", 123, [67.89, 2])
        self.assertEqual(myAirport.latitude, 0)
        self.assertEqual(myAirport.longitude, 0)
        myAirport = Airport("TST", "TestAirport", "TestCity", "TestCountry", "abc", "def")
        self.assertEqual(myAirport.latitude, 0)
        self.assertEqual(myAirport.longitude, 0)
        myAirport = Airport("TST", "TestAirport", "TestCity", "TestCountry", (123, 24), "def")
        self.assertEqual(myAirport.latitude, 0)
        self.assertEqual(myAirport.longitude, 0)

    # Test to check creating string from airport name
    def testAirportString(self):
        self.assertEqual(str(self.testAirport), "TST: TestAirport Airport, TestCity, TestCountry")

if __name__ == '__main__':
    unittest.main()
