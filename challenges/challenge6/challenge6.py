import unittest
from challenges.copart import copartPages


class Challenge6(unittest.TestCase):
    def setUp(self):
        self.driver = copartPages.DriverFactory.build_driver("chrome", __name__);

    def tearDown(self):
        self.driver.close()

    def test_challenge6(self):
        homepage = copartPages.Homepage(self.driver)
        homepage.navigate()
        homepage.do_search("Nissan")
        results_page = copartPages.ResultsPage(self.driver)
        results_page.wait_for_page_load()
        results_page.set_filter("Model", "Skyline")


if __name__ == '__main__':
    unittest.main()
