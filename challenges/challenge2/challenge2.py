import unittest
from selenium import webdriver
from challenges.copart import copartPage


class Challenge2(unittest.TestCase):
    def setUp(self):
        driver_path = "../chromedriver.exe" if __name__ == 'challenge2' else "chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        homepage = copartPage.Homepage(self.driver)
        homepage.navigate()
        homepage.do_search("exotics")
        results_page = copartPage.ResultsPage(self.driver)
        results_page.wait_for_page_load()
        models = results_page.get_results_by_column("make")
        self.assertIn("PORSCHE", models)


if __name__ == '__main__':
    unittest.main()
