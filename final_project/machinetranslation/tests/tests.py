"""
Testing Translation Module
"""
import unittest
from translator import english_to_french, french_to_english


class TestTranslator(unittest.TestCase):
    """
    Testing eng to fr and vice-versa
    """
    def test_english_to_french(self):
        """
        :return: Eng To Fr Translation
        """
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Hello')

    def test_french_to_english(self):
        """
        :return: Fr To Eng Translation
        """
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Bonjour'), 'Bonjour')


unittest.main()
