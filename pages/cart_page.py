from selenium.webdriver.common.by import By
from pages.core_app_page import CoreAppPage
from pages.checkout_pages import CheckoutStepOnePage


class CartPage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/cart.html'
        self.items_list = (By.CLASS_NAME, 'cart_item')
        self.secondary_header_title = (By.CLASS_NAME, 'title')
        self.remove_buttons = (By.CLASS_NAME, 'cart_button')
        self.back_button = (By.ID, 'continue-shopping')
        self.checkout_button = (By.ID, 'checkout')

    def checkout_order(self):
        self.scroll_and_click(self.driver.find_element(*(self.checkout_button)))
        checkout_page = CheckoutStepOnePage(self.driver)
        assert checkout_page.url == self.driver.current_url
        return checkout_page
