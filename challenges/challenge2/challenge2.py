import unittest
from challenges.copart import copartPages


class Challenge2(unittest.TestCase):
    def setUp(self):
        self.driver = copartPages.DriverFactory.build_driver("chrome", __name__);

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        homepage = copartPages.Homepage(self.driver)
        homepage.navigate()
        homepage.do_search("exotics")
        results_page = copartPages.ResultsPage(self.driver)
        results_page.wait_for_page_load()
        makes = results_page.get_results_by_column("make")
        self.assertIn("PORSCHE", makes)


if __name__ == '__main__':
    unittest.main()
