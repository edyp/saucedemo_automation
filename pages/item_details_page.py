from selenium.webdriver.common.by import By
from pages.core_app_page import CoreAppPage


class ItemDetailsPage(CoreAppPage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = 'https://www.saucedemo.com/inventory-item.html'
        self.add_button = (By.CLASS_NAME, 'btn_inventory')
        self.back_button = (By.ID, 'back-to-products')

    def click_add_remove_button(self):
        """Click on button that adds or removes from cart the item."""
        self.driver.find_element(*(self.add_button)).click()

    def click_back_button(self):
        """Click back button to get back to products list."""
        self.driver.find_element(*(self.back_button)).click()

    def add_to_cart_and_back(self):
        """Sequence of actions to add product to cart and get back to products list."""
        self.click_add_remove_button()
        assert self.driver.find_element(*(self.add_button)).text == 'Remove'
        self.click_back_button()

    def remove_from_cart_and_back(self):
        """Sequence of actions to remove product from cart and get back to products list."""
        self.click_add_remove_button()
        assert self.driver.find_element(*(self.add_button)).text == 'Add to cart'
        self.click_back_button()
