import unittest
from challenges.challenge4.fibo import fibonacci


class Challenge4(unittest.TestCase):
    def test_challenge4(self):
        fibo11 = fibonacci(11)
        print(fibo11)
        self.assertEqual(fibo11, '89 - eighty nine')

        fibo62 = fibonacci(62)
        print(fibo62)
        self.assertEqual(fibo62, '4052739537881 - four trillion fifty two billion seven hundred thirty nine million'
                                 ' five hundred thirty seven thousand eight hundred eighty one')


if __name__ == '__main__':
    unittest.main()
