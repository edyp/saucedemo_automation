import random
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.item_details_page import ItemDetailsPage


INDEX_1, INDEX_2 = tuple(random.sample(range(0, 5), 2))

def test_add_2_items_to_cart_on_items_list_page(driver, default_credentials):
    inventory = LoginPage(driver).login(default_credentials[0]['username'],
                                        default_credentials[0]['password'])
    inventory.reset_app_state()
    avaible_items = driver.find_elements(*(inventory.add_to_cart_buttons))
    cart = driver.find_element(*(inventory.cart))
    inventory.scroll_and_click(avaible_items[INDEX_1])
    inventory.scroll_and_click(avaible_items[INDEX_2])
    assert cart.text == '2'
    avaible_items = driver.find_elements(*(inventory.add_to_cart_buttons))
    assert avaible_items[INDEX_1].text == 'Remove'
    assert avaible_items[INDEX_2].text == 'Remove'

def test_remove_2_items_from_cart_on_items_list_page(driver):
    inventory = InventoryPage(driver)
    avaible_items = driver.find_elements(*(inventory.add_to_cart_buttons))
    cart = driver.find_element(*(inventory.cart))
    inventory.scroll_and_click(avaible_items[INDEX_1])
    assert cart.text == '1'
    inventory.scroll_and_click(avaible_items[INDEX_2])
    assert cart.text == ''
    avaible_items = driver.find_elements(*(inventory.add_to_cart_buttons))
    assert avaible_items[INDEX_1].text == 'Add to cart'
    assert avaible_items[INDEX_2].text == 'Add to cart'

def test_add_2_items_to_cart_on_item_details_page(driver):
    inventory = InventoryPage(driver)
    avaible_items = driver.find_elements(*(inventory.items_img))
    inventory.scroll_and_click(avaible_items[INDEX_1])
    item_page = ItemDetailsPage(driver)
    assert item_page.url in driver.current_url
    item_page.add_to_cart_and_back()
    assert inventory.url == driver.current_url
    assert driver.find_element(*(inventory.cart)).text == '1'

    avaible_items = driver.find_elements(*(inventory.items_img))
    inventory.scroll_and_click(avaible_items[INDEX_2])
    assert item_page.url in driver.current_url
    item_page.add_to_cart_and_back()
    assert inventory.url == driver.current_url
    assert driver.find_element(*(inventory.cart)).text == '2'

def test_remove_2_items_from_cart_on_item_details_page(driver):
    inventory = InventoryPage(driver)
    avaible_items = driver.find_elements(*(inventory.items_img))
    inventory.scroll_and_click(avaible_items[INDEX_1])
    item_page = ItemDetailsPage(driver)
    assert item_page.url in driver.current_url
    item_page.remove_from_cart_and_back()
    assert inventory.url == driver.current_url
    assert driver.find_element(*(inventory.cart)).text == '1'

    avaible_items = driver.find_elements(*(inventory.items_img))
    inventory.scroll_and_click(avaible_items[INDEX_2])
    assert item_page.url in driver.current_url
    item_page.remove_from_cart_and_back()
    assert inventory.url == driver.current_url
    assert driver.find_element(*(inventory.cart)).text == ''
