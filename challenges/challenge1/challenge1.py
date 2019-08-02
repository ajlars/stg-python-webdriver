import unittest
from selenium import webdriver


class Challenge1(unittest.TestCase):
    def setUp(self):
        driver_path = "../chromedriver.exe" if __name__ == 'challenge1' else "chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


if __name__ == '__main__':
    unittest.main()
