from Address import *

import unittest
     
class KirksvilleAddress(unittest.TestCase):
    

    def testNormalization(self):
        hillcrest_address = Address("303? North Hillcrest, Drive.", "Kirksville", "missouri", "63501")
        hillcrest_address.normalize()
        self.assertEqual(hillcrest_address.getStreet(), "303 N HILLCREST DR")
        self.assertEqual(hillcrest_address.getCity(), "KIRKSVILLE")
        self.assertEqual(hillcrest_address.getState(), "MO")

    def testDirectionStreet(self):
        directionStreet = Address("100 West Street", "Kirksville", "MO", "63501");  
        directionStreet.normalize()
        self.assertEqual(directionStreet.getStreet(), "100 WEST ST")

    def testDirectionSuffix(self):
        directionSuffix = Address("100 test street south", "", "", "")
        directionSuffix.normalize()
        self.assertEqual(directionSuffix.getStreet(), "100 TEST ST S")
        directionSuffix = Address("100 test street southWEST", "", "", "")
        directionSuffix.normalize()
        self.assertEqual(directionSuffix.getStreet(), "100 TEST ST SW")

    def testAbbrevFile(self):
        abbrev = Address("", "", "", "")
        abbreviations = abbrev.getAbbrevs("suffixAbbreviations.txt")
        self.assertEqual(abbreviations["ALLEY"], "ALY")
        self.assertEqual(abbreviations["WELLS"], "WLS")

    def testStateAbbrevFile(self):
        abbrev = Address("", "", "", "")
        abbreviations = abbrev.getAbbrevs("stateAbbreviations.txt")
        self.assertEqual(abbreviations["MISSOURI"], "MO")
        self.assertEqual(abbreviations["FEDERATED STATES OF MICRONESIA"], "FM")


if __name__ == '__main__':
    unittest.main()
