"""
This test is for machinetranslation
"""
import unittest
from ..translator import french_to_english , english_to_french


class TestsEnglishToFrench(unittest.TestCase):
    """
    Class to test the function english_to_french
    """

    def test1(self):
        """
        Function to test the function english_to_french
        """
        self.assertIsNone(english_to_french(None))
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Bonjour"), "Hello")


class TestsFrenchToEnglish(unittest.TestCase):
    """
    Class to test the function french_to_english
    """

    def test1(self):
        """
        Function to test the function french_to_english
        """
        self.assertIsNone(french_to_english(None))
        self.assertEqual(french_to_english("Bonjour"), "Hello")
        self.assertNotEqual(french_to_english("Hello"), "Bonjour")


unittest.main()
