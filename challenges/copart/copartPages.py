import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class DriverFactory(object):
    # calling_name is necessary: if the call is coming in from challengeSuite.py,
    # names will be challenges.challenge1.challenge1 etc
    # otherwise, from individual files, it wil be file names like challenge1
    @staticmethod
    def build_driver(browser, calling_name):
        if browser == "chrome":
            driver_path = os.path.abspath("chromedriver.exe" if "." in calling_name else "../chromedriver.exe")
            driver = webdriver.Chrome(driver_path)
        elif browser == "firefox":
            driver_path = os.path.abspath("geckodriver.exe" if "." in calling_name else "../geckodriver.exe")
            driver = webdriver.Firefox(executable_path=driver_path)
        return driver


class BasePage(object):
    url = None
    unique_element = {
        "method": None,
        "selector": None
    }

    def __init__(self, driver):
        self.driver = driver

    def fill_form_by_css(self, form_css, value):
        elem = self.driver.find_element_by_css_selector(form_css)
        elem.send_keys(value)

    def fill_form_by_id(self, form_element_id, value):
        elem = self.driver.find_element_by_id(form_element_id)
        elem.send_keys(value)

    def navigate(self):
        self.driver.get(self.url)
        self.wait_for_page_load()

    def get_text_from_elements(self, elements_selector):
        time.sleep(.25)
        elems = self.driver.find_elements_by_xpath(elements_selector)
        results = []
        for elem in elems:
            results.append(elem.text)

        return results

    def get_attr_from_elements(self, elements_selector, attr):
        elems = self.driver.find_elements_by_xpath(elements_selector)
        results = []
        for elem in elems:
            results.append(elem.get_attribute(attr))

        return results

    def wait_for_page_load(self):
        self.wait_for_element(self.unique_element.get('method'), self.unique_element.get('selector'))

    def wait_for_element(self, method, selector):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((method, selector))
            )
        except TimeoutError:
            print(f"Element '{selector}' not found with method '{method}'")


class Homepage(BasePage):
    url = "http://copart.com"
    unique_element = {
        "method": By.XPATH,
        "selector": "//li[@class='active']/a[@href='./']"
    }

    def do_search(self, search):
        """
        Do a search.
        :param search: string to search by
        """
        self.fill_form_by_id("input-search", search)
        self.driver.find_element_by_css_selector("button[data-uname='homepageHeadersearchsubmit']").click()

    def get_popular_items(self):
        popular_items_xpath = "//div[@ng-if='popularSearches']//a"
        item_names = self.get_text_from_elements(popular_items_xpath)
        item_links = self.get_attr_from_elements(popular_items_xpath, 'href')
        results = []

        for i, name in enumerate(item_names, start=0):
            results.append({
                "name": name,
                "url": item_links[i]
            })

        return results


class ResultsPage(BasePage):
    unique_element = {
        "method": By.CSS_SELECTOR,
        "selector": "[ng-if='searchText']"
    }

    def get_search_string(self):
        search_string_selector = "[ng-if='searchText']"
        self.wait_for_element(By.CSS_SELECTOR, search_string_selector)
        return self.driver.find_element_by_css_selector(search_string_selector).text

    def get_not_found_string(self):
        not_found_selector = "[data-uname='sorryMessage']"
        self.wait_for_element(By.CSS_SELECTOR, not_found_selector)
        return self.driver.find_element_by_css_selector(not_found_selector).text

    def set_result_max(self, limit):
        wait = WebDriverWait(self.driver, 10)
        self.driver.find_element_by_xpath(
            f"(//select[@name='serverSideDataTable_length'])[1]/option[@value='{limit}']").click()
        time.sleep(1)

    def set_filter(self, category, checkbox):
        filter_selector = f"(//div[@class='filter-inner']//a[@data-toggle='collapse'])[contains(text(), '{category}')]"
        self.wait_for_element(By.XPATH, filter_selector)
        filter_category = self.driver.find_element_by_xpath(filter_selector)
        selected = False
        filter_expanded = filter_category.get_attribute('aria-expanded')
        if filter_expanded is None or filter_expanded != "True":
            filter_category.click()
        category_filters = self.driver.find_elements_by_xpath(
            f"(//div[@class='filter-inner']//a[@data-toggle='collapse'])[contains(text(), '{category}')]/../..//abbr")
        try:
            for element in category_filters:
                if not selected:
                    label = element.text.strip()
                    if label == checkbox:
                        selected = True
                        element.click()
            if not selected:
                raise Exception(f"Filter: '{checkbox}' not found.")
        except Exception as error:
            self.driver.save_screenshot(f"../error_screenshots/filterNotFound{int(time.time())}.png")

    def get_results_by_column(self, column_name):
        """
        Get the text values from a results list column.
        :param column_name: Case insensitive, Year, Make, Model, Item#, Location / Lane / Row
                            Sale Date, Odometer, Doc Type, Damage, Est. Retail Value, or Current Bid
        :return: textual values of the cells in the column
        """
        col_numbers = {
            "year": 4,
            "make": 5,
            "model": 6,
            "item#": 7,
            "location / lane / row": 8,
            "sale date": 9,
            "odometer": 10,
            "doc type": 11,
            "damage": 12,
            "est. retail value": 13,
            "current bid": 14
        }
        my_col = col_numbers.get(column_name.lower(), False)
        if my_col:
            selector = f"//*[@id='serverSideDataTable']//tr/td[{my_col}]"
            self.wait_for_element(By.XPATH, f'({selector})[1]')
            return self.get_text_from_elements(selector)
        else:
            print(f"Column title '{column_name}' did not match any available columns.")
            return []
