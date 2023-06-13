import pytest
from pages.login_page import LoginPage
from pages.cart_page import CartPage


def test_add_item_to_cart(driver, default_credentials):
    inventory = LoginPage(driver).login(default_credentials[0]['username'],
                                        default_credentials[0]['password'])
    inventory.reset_app_state()
    item_button = driver.find_element(*(inventory.add_to_cart_buttons))
    cart = driver.find_element(*(inventory.cart))
    inventory.scroll_and_click(item_button)
    assert cart.text == '1'
    cart.click()
    cart_page = CartPage(driver)
    assert cart_page.url == driver.current_url
    cart_items = driver.find_elements(*(cart_page.items_list))
    assert 1 == len(cart_items)

def test_checkout_order(driver, personal_data):
    cart_page = CartPage(driver)
    checkout_step_one = cart_page.checkout_order()
    data = personal_data.pop()
    checkout_step_one.fill_form(data['first_name'],
                                data['last_name'],
                                data['postal_code']
                                )
    checkout_step_two = checkout_step_one.next_step()
    checkout_step_two.check_item_total_price()
    checkout_step_two.check_total_price()

    labels_web_elems = driver.find_elements(*(checkout_step_two.summary_labels))
    labels = [x.text for x in labels_web_elems]
    expected_labels = ['Payment Information',
                       'Shipping Information',
                       'Price Total',
                       'Total:']
    for label, exp_label in zip(labels, expected_labels):
        assert exp_label in label
    
    checkout_completed = checkout_step_two.finish_order()
    checkout_completed.assert_order_confirmed()
    inventory_page = checkout_completed.click_back_button()
    inventory_page.assert_page_loaded()
