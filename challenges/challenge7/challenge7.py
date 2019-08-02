import unittest
from selenium import webdriver
from challenges.copart import copartPage


class Challenge7(unittest.TestCase):
    def setUp(self):
        driver_path = "../chromedriver.exe" if __name__ == 'challenge7' else "chromedriver.exe"
        self.driver = webdriver.Chrome(driver_path)

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        homepage = copartPage.Homepage(self.driver)
        homepage.navigate()
        popular_items = homepage.get_popular_items()
        results_page = copartPage.ResultsPage(self.driver)
        for item in popular_items:
            self.driver.get(item.get('url'))
            results_page.wait_for_page_load()
            search_string = results_page.get_search_string().lower()
            should_contain = item.get('name').replace(' ', '-').lower()
            current_url = self.driver.current_url.lower()
            self.assertIn(should_contain, search_string, "The search text didn't include {should_contain}")
            self.assertIn(should_contain, current_url, "The url didn't include {should_contain}")


if __name__ == '__main__':
    unittest.main()
