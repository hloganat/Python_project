from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys
from src.Page_Elements.pages import Pages

def test_open_url():

    driver = webdriver.Chrome(r'C:\Users\hari4\aldo-webui-python-selenium\chromedriver')
    # Opens a known doi url
    driver.get("https://www.aldoshoes.com")
    driver.maximize_window()

    page = Pages(driver)
    # Gives the browser a few seconds to process the redirect
    time.sleep(3)

    # Retrieves the url after the redirect
    title = driver.title
    driver.maximize_window()

    print(driver.current_url)
    print(title)
    assert title == "ALDO Canada | ALDO Shoes, Boots, Sandals, Handbags & Accessories"

    locator_dict = Pages.collect_locators()
    print(locator_dict)

    #click on the category button
    page.click_action_button(locator_dict.get('women_button'))
    time.sleep(2)

    filter_text = page.get_Filter_element(locator_dict.get('filter_button')).text
    assert filter_text == "Filter"

    driver.close()

