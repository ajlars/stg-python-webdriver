import unittest
from selenium import webdriver
from challenges.copart import copartPage


class Challenge6(unittest.TestCase):
    def setUp(self):
        driver_path = "../chromedriver.exe" if __name__ == 'challenge6' else "chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        homepage = copartPage.Homepage(self.driver)
        homepage.navigate()
        homepage.do_search("Nissan")
        results_page = copartPage.ResultsPage(self.driver)
        results_page.wait_for_page_load()
        results_page.set_filter("Model", "Skyline")


if __name__ == '__main__':
    unittest.main()
