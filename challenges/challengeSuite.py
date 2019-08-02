import unittest
from challenges.challenge1 import challenge1
from challenges.challenge2 import challenge2
from challenges.challenge3 import challenge3
from challenges.challenge4 import challenge4
from challenges.challenge5 import challenge5
from challenges.challenge6 import challenge6
from challenges.challenge7 import challenge7


def suite():
    suite = unittest.TestSuite()

    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge1))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge2))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge3))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge4))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge5))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge6))
    suite.addTest(unittest.TestLoader().loadTestsFromModule(challenge7))
    return suite


if __name__ == '__main__':
    unittest.main(defaultTest='suite')
