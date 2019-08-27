import unittest
from challenges.copart import copartPages


class Challenge7(unittest.TestCase):
    def setUp(self):
        self.driver = copartPages.DriverFactory.build_driver("chrome", __name__);

    def tearDown(self):
        self.driver.close()

    def test_challenge7(self):
        homepage = copartPages.Homepage(self.driver)
        homepage.navigate()
        popular_items = homepage.get_popular_items()
        results_page = copartPages.ResultsPage(self.driver)
        for item in popular_items:
            self.driver.get(item.get('url'))
            results_page.wait_for_page_load()
            search_string = results_page.get_search_string().lower()
            string_to_find = item.get('name').replace(' ', '-').lower()
            current_url = self.driver.current_url.lower()
            self.assertIn(string_to_find, current_url, f"The url didn't include {string_to_find}")
            if string_to_find in search_string:
                self.assertIn(string_to_find, search_string, f"The search text didn't include {string_to_find}")
            else:
                not_found_string = results_page.get_not_found_string()
                self.assertIn(string_to_find, not_found_string, f"The not found text didn't include {string_to_find}")



if __name__ == '__main__':
    unittest.main()
