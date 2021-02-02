import csv
import os
import traceback

import pytest
import pprint

from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains


class Pages:
    def __init__(self, driver):
        self.driver = driver

    @staticmethod
    def collect_locators():
        locator_dir = os.path.dirname(os.path.abspath("page_locators.csv"))
        locator_file = os.path.join(locator_dir, "Page_Locators")
        csv_path = os.path.join(locator_file, 'page_locators.csv')
        reader = csv.DictReader(open(csv_path, 'r'))
        dict_locator = {}
        for line in reader:
            dict_locator.update({line.get('element_name'): line.get('xpath')})
        return dict_locator

    def click_action_button(self, item_xpath):
        wait = WebDriverWait(self.driver, 10)
        print("Clicking on %s" % item_xpath)
        try:
            button_element = wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
            ActionChains(self.driver).click(button_element).perform()
        except TimeoutException:
            print("Loading took too much time!")

    def get_Filter_element(self, filter_xpath):
        try:
            wait = WebDriverWait(self.driver, 30)
            timeout: int = 30
            #   print("Clicking on Filter button")
            web_element = wait.until(EC.presence_of_element_located((By.XPATH, filter_xpath)))
            return web_element
        except TimeoutException as err:
            print("Timed out waiting for Filter button")
            # webdriver.close()

    def click_On_Filter_button(self, filter_xpath):
        wait = WebDriverWait(self.driver, 10)
        print("Clicking on filter button", filter_xpath)
        try:
            button_element = wait.until(EC.element_to_be_clickable((By.XPATH, filter_xpath)))
            ActionChains(self.driver).click(button_element).perform()
        except TimeoutException:
            print("Loading took too much time!")

    def click_list_option_button(self, item_xpath):
        wait = WebDriverWait(self.driver, 10)
        print("Clicking on %s" % item_xpath)
        try:
            list_option_element = wait.until(EC.element_to_be_clickable((By.XPATH, item_xpath)))
            self.driver.implicitly_wait(10)
            self.driver.execute_script("arguments[0].click()", list_option_element)
        except TimeoutException:
            print("Loading took too much time!")

    def check_or_uncheck_box(self, item_xpath):
        print("Clicking on %s" % item_xpath)
        checkbox = self.driver.find_element(By.XPATH, item_xpath)
        self.scroll_element_into_view(self.driver, checkbox)

    def scroll_element_into_view(self, driver, element):
        """Scroll element into view"""
        y = element.location['y']
        driver.execute_script('window.scrollTo(0, {0})'.format(y))
        driver.implicitly_wait(10)
        driver.execute_script("arguments[0].click()", element)
