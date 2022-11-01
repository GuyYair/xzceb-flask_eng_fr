import unittest

from translator import english_to_french, french_to_english

class Test_e2f(unittest.TestCase): 
    def test1(self): 
        self.assertEqual(english_to_french(""),"Nullinput") 
        self.assertEqual(english_to_french('Hello'),'Bonjour')

class Test_f2e(unittest.TestCase): 
    def test2(self):
        self.assertEqual(french_to_english(""),"Nullinput")  
        self.assertEqual(french_to_english('Bonjour'),'Hello')

unittest.main()