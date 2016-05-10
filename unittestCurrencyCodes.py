import unittest
from CurrencyCodes import CurrencyDict

class testCurrencyDictClass(unittest.TestCase):
    """Unit tests for CurrencyDict class"""
    def setUp(self):
        self.testCurrencyDict = CurrencyDict("countrycurrency.csv")

    # Test to check if valid csv file can be loaded
    def testValidCsvFile(self):
        self.assertEqual(len(self.testCurrencyDict.currencies), 249)    # Check if all lines of file have been read

    # Test to check if non-csv file can be loaded
    def testNonCsvFile(self):
        myCurrencies = CurrencyDict("Currency.py")
        self.assertEqual(myCurrencies.currencies, {})

    # Test to check if non-existent csv file can be loaded
    def testNonExistentCsvFile(self):
        myCurrencies = CurrencyDict("myFile.csv")
        self.assertEqual(myCurrencies.currencies, {})

    # Test to check if invalid csv file can be loaded
    def testInvalidCsvFile(self):
        myCurrencies = CurrencyDict("airport.csv")
        self.assertEqual(myCurrencies.currencies, {})
        myCurrencies = CurrencyDict("aircraft.csv")
        self.assertEqual(myCurrencies.currencies, {})
        myCurrencies = CurrencyDict("testroutes.csv")
        self.assertEqual(myCurrencies.currencies, {})
        myCurrencies = CurrencyDict("currencyrates.csv")
        self.assertEqual(myCurrencies.currencies, {})

    # Test to check look up of valid currencies
    def testValidCurrencies(self):
        currency = self.testCurrencyDict.getCurrency("Ireland")
        self.assertEqual(str(currency), "EUR: Euro")
        currency = self.testCurrencyDict.getCurrency("Malawi")
        self.assertEqual(str(currency), "MWK: Kwacha")
        currency = self.testCurrencyDict.getCurrency("Saint Lucia")
        self.assertEqual(str(currency), "XCD: East Caribbean Dollar")

    # Test to check look up of invalid currencies
    def testInValidCurrencies(self):
        currency = self.testCurrencyDict.getCurrency("Heaven")
        self.assertEqual(currency, 0)
        currency = self.testCurrencyDict.getCurrency([12, 4])
        self.assertEqual(currency, 0)
        currency = self.testCurrencyDict.getCurrency({"a": 1, "b": 2})
        self.assertEqual(currency, 0)




if __name__ == '__main__':
    unittest.main()
