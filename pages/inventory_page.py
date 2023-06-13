from selenium.webdriver.common.by import By
from pages.core_app_page import CoreAppPage


class InventoryPage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/inventory.html'
        self.products_header = (By.CLASS_NAME, 'header_secondary_container')
        self.sort_dropdown = (By.CLASS_NAME, 'product_sort_container')
        self.active_sort_opt = (By.CLASS_NAME, 'active_option')
        self.products_list = (By.CLASS_NAME, 'inventory_container')
        self.items = (By.CLASS_NAME, 'inventory_item')
        self.items_label = (By.CLASS_NAME, 'inventory_item_label')
        self.items_img = (By.CLASS_NAME, 'inventory_item_img')
        self.add_to_cart_buttons = (By.CLASS_NAME, 'btn_inventory')

    def assert_page_loaded(self):
        assert self.url == self.driver.current_url
        self.assert_header()
        assert self.driver.find_element(*(self.products_header)).is_displayed()
        assert self.driver.find_element(*(self.products_list)).is_displayed()