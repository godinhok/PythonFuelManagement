import unittest
from ExchangeRates import *

class testExchangeRatesClass(unittest.TestCase):
    """Unit tests for Exchange Rates class"""
    def setUp(self):
        self.testExchangeRates = ExchangeRates("currencyrates.csv")
        self.testRate = Rate("TST", 0.4, 2.5)

    # Test to check that attributes of rate are set up correctly
    def testRateAttributes(self):
        self.assertEqual(self.testRate.code, "TST")
        self.assertEqual(self.testRate.toEuro, 0.4)
        self.assertEqual(self.testRate.fromEuro, 2.5)

    # Test to check printing a string of currency rate
    def testStringRate(self):
        self.assertEqual(str(self.testRate), "1 EUR = 0.4 TST; 1 TST = 2.5 EUR")

    # Test to check if valid csv file can be loaded
    def testValidCsvFile(self):
        self.assertEqual(len(self.testExchangeRates.rates), 196)    # Check if all lines of file have been read

    # Test to check if non-csv file can be loaded
    def testNonCsvFile(self):
        myRates = ExchangeRates("Currency.py")
        self.assertEqual(myRates.rates, {})

    # Test to check if non-existent csv file can be loaded
    def testNotExistsCsvFile(self):
        myRates = ExchangeRates("Currency.csv")
        self.assertEqual(myRates.rates, {})

    # Test to check if invalid csv file can be loaded
    def testInvalidCsvFile(self):
        myRates = ExchangeRates("airport.csv")
        self.assertEqual(myRates.rates, {})
        myRates = ExchangeRates("aircraft.csv")
        self.assertEqual(myRates.rates, {})
        myRates = ExchangeRates("countrycurrency.csv")
        self.assertEqual(myRates.rates, {})

    # Test to check look up of valid currency rates
    def testValidRateLookup(self):
        rate = self.testExchangeRates.getRate("GBP")
        self.assertEqual(str(rate), "1 EUR = 1.4029 GBP; 1 GBP = 0.713 EUR")

    # Test to check look up of invalid currency rates
    def testInvalidRateLookup(self):
        rate = self.testExchangeRates.getRate("abc")
        self.assertEqual(rate, 0)
        rate = self.testExchangeRates.getRate([1,2])
        self.assertEqual(rate, 0)

    # Test to check conversion to and from Euro for valid currencies
    def testToEuroConvert(self):
        value = self.testExchangeRates.convertToEuro(1000, "GBP")
        self.assertEqual(value, 1402.9)
        value = self.testExchangeRates.convertToEuro(1000, "KHR")
        self.assertEqual(value, 0.2388)
        value = self.testExchangeRates.convertFromEuro(1000, "JMD")
        self.assertEqual(value, 123637)
        value = self.testExchangeRates.convertFromEuro(1000, "SKK")
        self.assertEqual(value, 30126)

    # Test to check conversion to and from Euro for invalid currencies
    def testInvalidCurrencyConvert(self):
        value = self.testExchangeRates.convertToEuro(1000, "abc")
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertToEuro(1000, [2, 3])
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertFromEuro(1000, "abc")
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertFromEuro(1000, [2, 3])
        self.assertEqual(value, 0)

    # Test to check conversion for invalid amounts
    def testInvalidAmountConvert(self):
        value = self.testExchangeRates.convertFromEuro("abc", "GBP")
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertToEuro("abc", "GBP")
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertToEuro([2, 3], "GBP")
        self.assertEqual(value, 0)
        value = self.testExchangeRates.convertFromEuro([2, 3], "GBP")
        self.assertEqual(value, 0)

if __name__ == '__main__':
    unittest.main()
