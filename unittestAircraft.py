import unittest
from Aircraft import Aircraft

class testAircraftClass(unittest.TestCase):
    """Unit tests for Aircraft class"""
    def setUp(self):
        self.testAircraft1 = Aircraft("A330", "metric", "Airbus", 13430)
        self.testAircraft2 = Aircraft("777", "imperial", "Boeing", 9700)

    # Test to check if aircraft attributes are set up for metric units
    def testMetricAttributes(self):
        self.assertEqual(self.testAircraft1.planeType, "A330")
        self.assertEqual(self.testAircraft1.manufacturer, "Airbus")
        self.assertEqual(self.testAircraft1.range, 13430)
        self.assertEqual(self.testAircraft1.MIN_FUEL, 1000)
        self.assertEqual(self.testAircraft1.maxFuel, 13430)

    # Test to check aircraft attributes are correct for imperial units
    def testImperialAttributes(self):
        self.assertEqual(self.testAircraft2.planeType, "777")
        self.assertEqual(self.testAircraft2.manufacturer, "Boeing")
        self.assertEqual(self.testAircraft2.range, 15607.3)
        self.assertEqual(self.testAircraft2.MIN_FUEL, 1000)
        self.assertEqual(self.testAircraft2.maxFuel, 15607.3)

    # Test to check strings of Aircraft class
    def testString(self):
        self.assertEqual(str(self.testAircraft1), "Airbus A330")
        self.assertEqual(str(self.testAircraft2), "Boeing 777")

    # Test to check for invalid units given on aircraft setup
    def testUnits(self):
        testAircraft = Aircraft("A330", "bob", "Airbus", 13430)
        self.assertEqual(testAircraft.range, 13430)

    # Test to check for units given as wrong data type
    def testUnitDataType(self):
        testAircraft = Aircraft("A330", "metric", "Airbus", "abc")
        self.assertEqual(testAircraft.range, 0)
        testAircraft = Aircraft("A330", "metric", "Airbus", [12, 13])
        self.assertEqual(testAircraft.range, 0)
        testAircraft = Aircraft("A330", "metric", "Airbus", self.testAircraft2)
        self.assertEqual(testAircraft.range, 0)

    # Test to check adding amount of fuel less than maximum fuel level
    def testAddLessFuel(self):
        self.testAircraft1.addFuel(5000)
        self.assertEqual(self.testAircraft1.getFuel(), 5000)
        self.testAircraft1.addFuel(3000)
        self.assertEqual(self.testAircraft1.getFuel(), 8000)

    # Test to check adding amount of fuel greater than maximum fuel level
    def testAddMoreFuel(self):
        fuelOver = self.testAircraft1.addFuel(20000)
        self.assertEqual(fuelOver, 6570)

    # Test to check adding fuel less than zero
    def testSyphonFuel(self):
        self.testAircraft1.addFuel(-5000)
        self.assertEqual(self.testAircraft1.getFuel(), 0)

    # Test to check adding fuel where volume is of incorrect data type
    def testAddFuelAsString(self):
        self.testAircraft1.addFuel("abc")   # Volume as string
        self.assertEqual(self.testAircraft1.getFuel(), 0)
        self.testAircraft1.addFuel([123, 345])  # Volume as list
        self.assertEqual(self.testAircraft1.getFuel(), 0)
        self.testAircraft1.addFuel((123, 345))  # Volume as tuple
        self.assertEqual(self.testAircraft1.getFuel(), 0)
        self.testAircraft1.addFuel(self.testAircraft2)  # Volume as object
        self.assertEqual(self.testAircraft1.getFuel(), 0)

    # Test to check that aircraft can use fuel
    def testUseFuel(self):
        self.testAircraft1.addFuel(13000)
        self.testAircraft1.useFuel(3000)
        self.assertEqual(self.testAircraft1.getFuel(), 10000)
        self.testAircraft1.useFuel(4500)
        self.assertEqual(self.testAircraft1.getFuel(), 5500)

    # Test to check using invalid amounts of fuel
    def testUseInvalidFuel(self):
        self.testAircraft1.addFuel(13000)
        self.testAircraft1.useFuel(-3000)   # Test negative amount of fuel
        self.assertEqual(self.testAircraft1.getFuel(), 13000)
        self.testAircraft1.useFuel("abc")   # Test adding string value as fuel
        self.assertEqual(self.testAircraft1.getFuel(), 13000)
        self.testAircraft1.useFuel([123, 24])   # Test using list to add fuel
        self.assertEqual(self.testAircraft1.getFuel(), 13000)

if __name__ == '__main__':
    unittest.main()
