import unittest
from Currency import Currency

class testCurrency(unittest.TestCase):
    """Unit tests for Currency class"""
    def setUp(self):
        self.testMoney = Currency("Iran", "Iranian Rial", "IRR")

    # Test to check currency object is setup with country, name and code
    def testCurrencySetup(self):
        self.assertEqual(self.testMoney.country, "Iran")
        self.assertEqual(self.testMoney.name, "Iranian Rial")
        self.assertEqual(self.testMoney.code, "IRR")

    # Test to check string for currency object
    def testCurrencyString(self):
        self.assertEqual(str(self.testMoney), "IRR: Iranian Rial")



if __name__ == '__main__':
    unittest.main()
