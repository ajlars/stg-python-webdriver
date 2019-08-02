import unittest
from selenium import webdriver
from challenges.copart import copartPage


class Challenge3(unittest.TestCase):
    def setUp(self):
        driver_path = "../chromedriver.exe" if __name__ == 'challenge3' else "chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        homepage = copartPage.Homepage(self.driver)
        homepage.navigate()
        popular_items = homepage.get_popular_items()
        for item in popular_items:
            print(f"{item.get('name')} - {item.get('url')}")


if __name__ == '__main__':
    unittest.main()
