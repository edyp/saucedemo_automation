from time import sleep
from selenium.webdriver.common.by import By
from common.logger import Logger


class CoreAppPage:
    LOG = Logger()

    def __init__(self, driver):
        self.driver = driver
        self.side_bar = SideBar(driver)
        self.header = (By.CLASS_NAME, 'primary_header')
        self.logo = (By.CLASS_NAME, 'app_logo')
        self.cart = (By.ID, 'shopping_cart_container')

    def logout(self):
        self.side_bar.show().logout()

    def assert_header(self):
        assert self.driver.find_element(*(self.side_bar.hamburger)).is_displayed()
        assert self.driver.find_element(*(self.logo)).is_displayed()
        assert self.driver.find_element(*(self.cart)).is_displayed()


class SideBar():
    def __init__(self, driver):
        self.driver = driver
        self.hamburger = (By.ID, 'react-burger-menu-btn')
        self.burger_cross = (By.ID, 'react-burger-cross-btn')
        self.inventory_page_item = (By.ID, 'inventory_sidebar_link')
        self.about_page_item = (By.ID, 'about_sidebar_link')
        self.logout_item = (By.ID, 'logout_sidebar_link')
        self.reset_item = (By.ID, 'reset_sidebar_link')

    def show(self):
        self.driver.find_element(*(self.hamburger)).click()
        sleep(0.5) # required because sidebar animation take time
        return self

    def close(self):
        self.driver.find_element(*(self.burger_cross)).click()
    
    def logout(self):
        self.driver.find_element(*(self.logout_item)).click()
