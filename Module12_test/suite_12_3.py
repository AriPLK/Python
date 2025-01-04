import unittest
from unittest import TextTestRunner
import tests_12_1
import tests_12_2


testCS = unittest.TestSuite()
testCS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_1.RunnerTest))
testCS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_2.TournamentTest))
obj1 = TextTestRunner(verbosity=2)
tests_12_1.is_frozen = False
tests_12_2.is_frozen = True
obj1.run(testCS)
