import unittest
from translator import english_to_french,french_to_english

class Testenglish_to_french(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour') # Test when th input is Hello and output is Bonjour
        self.assertNotEqual(english_to_french('null'), 'null')

from translator import french_to_english

class Testfrench_to_english(unittest.TestCase):
    def test1(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello') # Test when th input is Bonjour and output is Hello
        self.assertNotEqual(french_to_english('null'), 'null')

    unittest.main()