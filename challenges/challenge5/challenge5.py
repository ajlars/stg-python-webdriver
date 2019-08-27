import unittest
from challenges.copart import copartPages


class Challenge5(unittest.TestCase):
    def setUp(self):
        self.driver = copartPages.DriverFactory.build_driver("chrome", __name__);

    def tearDown(self):
        self.driver.close()

    def test_challenge5(self):
        homepage = copartPages.Homepage(self.driver)
        homepage.navigate()
        homepage.do_search("Porsche")
        results_page = copartPages.ResultsPage(self.driver)
        results_page.wait_for_page_load()
        results_page.set_result_max(100)
        models = results_page.get_results_by_column("model")
        model_counts = {}
        for model in models:
            if model in list(model_counts):
                model_counts[model] = model_counts[model] + 1
            else:
                model_counts[model] = 1
        print('''
=====================
        MODELS
=====================
        ''')
        for model in list(model_counts):
            print(f'{model} was found {model_counts[model]} times.')

        self.subTest('Damage check')

        damages = results_page.get_results_by_column("damage")
        damage_counts = {"REAR END" : 0, "FRONT END": 0, "MINOR DENT/SCRATCHES": 0, "UNDERCARRIAGE": 0, "MISC": 0}
        damage_sorter = {
            "REAR END" : "REAR END",
            "FRONT END" : "FRONT END",
            "MINOR DENT/SCRATCHES": "MINOR DENT/SCRATCHES",
            "UNDERCARRIAGE": "UNDERCARRIAGE"
        }
        for damage in damages:
            name = damage_sorter.get(damage, "MISC")
            damage_counts[name] = damage_counts[name] + 1
        print('''
=====================
        DAMAGES
=====================
        ''')
        for damage in list(damage_counts):
            print(f'{damage} occurred {damage_counts[damage]} times.')


if __name__ == '__main__':
    unittest.main()
