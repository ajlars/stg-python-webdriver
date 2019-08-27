import unittest
from challenges.copart import copartPages


class Challenge3(unittest.TestCase):
    def setUp(self):
        self.driver = copartPages.DriverFactory.build_driver("chrome", __name__);

    def tearDown(self):
        self.driver.close()

    def test_challenge3(self):
        homepage = copartPages.Homepage(self.driver)
        homepage.navigate()
        popular_items = homepage.get_popular_items()
        for item in popular_items:
            print(f"{item.get('name')} - {item.get('url')}")


if __name__ == '__main__':
    unittest.main()
