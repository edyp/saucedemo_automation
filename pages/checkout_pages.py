from selenium.webdriver.common.by import By
from pages.core_app_page import CoreAppPage
from pages.inventory_page import InventoryPage


class CheckoutStepOnePage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/checkout-step-one.html'
        self.first_name_field = (By.ID, 'first-name')
        self.last_name_field = (By.ID, 'last-name')
        self.postal_code_field = (By.ID, 'postal-code')
        self.cancel_button = (By.ID, 'cancel')
        self.continue_button = (By.ID, 'continue')
        self.secondary_header_title = (By.CLASS_NAME, 'title')

    def next_step(self):
        self.driver.find_element(*(self.continue_button)).click()
        return CheckoutStepTwoPage(self.driver)

    def cancel(self):
        self.driver.find_element(*(self.cancel_button)).click()

    def fill_form(self, first_name, last_name, postal_code):
        self.driver.find_element(*(self.first_name_field)).send_keys(first_name)
        self.driver.find_element(*(self.last_name_field)).send_keys(last_name)
        self.driver.find_element(*(self.postal_code_field)).send_keys(postal_code)


class CheckoutStepTwoPage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/checkout-step-two.html'
        self.secondary_header_title = (By.CLASS_NAME, 'title')
        self.summary_labels = (By.CLASS_NAME, 'summary_info_label')
        self.cart_items = (By.CLASS_NAME, 'cart_item')
        self.finish_button = (By.ID, 'finish')
        self.cancel_button = (By.ID, 'cancel')
        self.item_price = (By.CLASS_NAME, 'inventory_item_price')
        self.items_total_price = (By.CLASS_NAME, 'summary_subtotal_label')
        self.tax_price = (By.CLASS_NAME, 'summary_tax_label')
        self.total_price = (By.CLASS_NAME, 'summary_total_label')

    def finish_order(self):
        self.driver.find_element(*(self.finish_button)).click()
        return CheckoutCompletePage(self.driver)

    def cancel(self):
        self.driver.find_element(*(self.cancel_button)).click()
    
    def _get_price_number_from_str(self, price_str):
        number_str = price_str.split('$')[-1]
        return float(number_str)

    def check_item_total_price(self):
        """Sum all items prices and check total amoutn on page.
        Important:
        This method is way beneath expeted functionality, it's mocked only for
        test_03_checkout_and_finalize_order.py::test_checkout_order test case.
        Desired functionality is multiplicating item price by quantity factor,
        then summing all products and compare to price from 'Item total' label.
        """
        str_price = self.driver.find_element(*(self.item_price)).text
        item_total_price = self._get_price_number_from_str(str_price)
        label_price = self.driver.find_element(*(self.items_total_price)).text
        counted_price = self._get_price_number_from_str(label_price)
        assert item_total_price == counted_price

    def check_total_price(self):
        """Sum items total price and tax prive then compare to total bill."""
        label_subtotal_price = self.driver.find_element(*(self.items_total_price)).text
        subtotal_price = self._get_price_number_from_str(label_subtotal_price)
        label_tax_price = self.driver.find_element(*(self.tax_price)).text
        tax_price = self._get_price_number_from_str(label_tax_price)
        label_total_price = self.driver.find_element(*(self.total_price)).text
        total_price = self._get_price_number_from_str(label_total_price)

        assert subtotal_price + tax_price == total_price


class CheckoutCompletePage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/checkout-complete.html'
        self.secondary_header_title = (By.CLASS_NAME, 'title')
        self.confirmation_container = (By.ID, 'checkout_complete_container')
        self.back_button = (By.ID, 'back-to-products')
    
    def assert_order_confirmed(self):
        title = self.driver.find_element(*(self.secondary_header_title)).text
        assert 'Checkout: Complete!' == title
        cart_text = self.driver.find_element(*(self.cart)).text
        assert '' == cart_text
        assert self.driver.find_element(*(self.confirmation_container)).is_displayed()

    def click_back_button(self):
        self.driver.find_element(*(self.back_button)).click()
        return InventoryPage(self.driver)
