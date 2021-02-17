from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.keys import Keys
from src.Page_Elements.pages import Pages
import csv

def csv_to_dict(input_file):
    reader = csv.DictReader(open(input_file, 'r'))
    dict_list = []
    for line in reader:
        dict_list.append(line)
    return dict_list

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

    input_file = "./input/input.csv"
    data = csv_to_dict(input_file)
    print(data)

    if data[0]['click_type'].lower() == 'button':
        if data[0]['gender'].lower() == 'women':
            # click on the category button
            page.click_action_button(locator_dict.get('women_button'))
            time.sleep(2)
        elif data[0]['gender'].lower() == 'men':
            page.click_action_button(locator_dict.get('men_button'))
            time.sleep(2)
        elif data[0]['gender'].lower() == "handbags":
            page.click_action_button(locator_dict.get('handbag_button'))
            time.sleep(2)
    else:
         page.hover_on_menu_element((locator_dict.get('menu_xpath') % data[0]['gender'].capitalize()))
         page.click_action_button(locator_dict.get('submenu_xpath') % data[0]['submenu_type'].capitalize())
    driver.set_page_load_timeout(5)
    time.sleep(2)
    filter_text = page.get_element(locator_dict.get('filter_button')).text
    assert filter_text == "Filter"

    page.click_On_Filter_button(locator_dict.get('filter_button'))

    filter_data = data[0]
    filter_list = ["Category", "size", "color", "price", "heel_height"]
    filter_dict = {}
    LIST_ITEM_FILTERS = ['size', 'colour']
    INPUT_ITEM_FILTERS = ['category', 'price', 'heel-height']
    for fv in filter_list:
        fv = fv.lower()
        if filter_data[fv]:
            if fv in INPUT_ITEM_FILTERS:
                page.check_or_uncheck_box(locator_dict.get('input_check_list') % (fv, filter_data[fv].lower()))
            else:
                page.click_list_option_button(locator_dict.get('filter_option_list') % (filter_data[fv].lower()))
    time.sleep(2)

    apply_filter_element = page.get_element(locator_dict.get('ApplyFilterTextButton')).text
    assert apply_filter_element == "Apply 2 filters"
    page.click_On_Filter_button(locator_dict.get('ApplyFilterTextButton'))
    image_elements = page.get_child_elements(locator_dict.get('productImageList'))
    page.click_on_child_element(image_elements, 0)
    page.click_On_Filter_button(locator_dict.get('addToBag'))
    time.sleep(5)
    # driver.close()
    # driver.quit()

