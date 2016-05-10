import unittest
from Itinerary import Itinerary

class testItineraryClass(unittest.TestCase):
    """Unit tests for Itinerary class"""
    def setUp(self):
        self.route = ["DUB", "HEA", "AAA", "MEL", "POL"]
        self.testItinerary1 = Itinerary(self.route, "747")

    # Test to check if itinerary attributes are correctly set up
    def testItineraryAttributes(self):
        self.assertEqual(self.testItinerary1.route, ["DUB", "HEA", "AAA", "MEL", "POL"])
        self.assertEqual(str(self.testItinerary1.aircraft), "Boeing 747")
        self.assertEqual(self.testItinerary1.revisitCode, "")

    # Test to check printing of itinerary string
    def testItineraryString(self):
        self.assertEqual(str(self.testItinerary1), "Route: {}; Aircraft: Boeing 747".format(self.route))

    # Test to check setting an aircraft in the itinerary
    def testSetValidAircraft(self):
        self.testItinerary1.setAircraft("777")
        self.assertEqual(str(self.testItinerary1.aircraft), "Boeing 777")

    # Test to check setting an invalid aircraft in the itinerary
    def testSetInvalidAircraft(self):
        self.testItinerary1.setAircraft("abc")
        self.assertEqual(str(self.testItinerary1.aircraft), "Boeing 747")

    # Test to check setting of revisit airport
    def testValidateRevisit(self):
        code = self.testItinerary1.validateRevisit("AAA")  # Valid revisit airport
        self.assertEqual(code, "AAA")
        code = self.testItinerary1.validateRevisit("a")  # Invalid revisit airport
        self.assertEqual(code, "")
        code = self.testItinerary1.validateRevisit([2,3])  # Invalid revisit airport
        self.assertEqual(code, "")


if __name__ == '__main__':
    unittest.main()
