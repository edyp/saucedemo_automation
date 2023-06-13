from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from common.logger import Logger


class CoreAppPage:
    LOG = Logger()

    def __init__(self, driver):
        self.driver = driver
        self.side_bar = SideBar(driver)
        self.header = (By.CLASS_NAME, 'primary_header')
        self.logo = (By.CLASS_NAME, 'app_logo')
        self.cart = (By.ID, 'shopping_cart_container')
        self._actions = ActionChains(self.driver)

    def logout(self):
        self.side_bar.show().logout()

    def reset_app_state(self):
        """Use functionality placed in side bar to reset the app state and
        and refresh page.
        """
        self.side_bar.show().reset_state()
        self.side_bar.close()
        self.driver.refresh()
    
    def scroll_and_click(self, element):
        """Scroll viewport to given element and click it.
        Parameters:
        element (WebElement): DOM element on page.
        """
        self._actions.move_to_element(element).click().perform()

    def assert_header(self):
        """Check all core app elements are visible on screen."""
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

    def reset_state(self):
        self.driver.find_element(*(self.reset_item)).click()