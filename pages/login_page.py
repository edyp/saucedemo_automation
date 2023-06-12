from selenium.webdriver.common.by import By
from common.logger import Logger
from pages.inventory_page import InventoryPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.saucedemo.com'
        self.log = Logger()

        self.username_field = (By.ID, 'user-name')
        self.password_field = (By.ID, 'password')
        self.login_button = (By.ID, 'login-button')
        self.credentials_wrap = (By.CLASS_NAME, 'login_credentials_wrap')

    def get_credentials(self):
        self.driver.get(self.url)
        text = self.driver.find_element(*(self.credentials_wrap)).text
        lines = text.splitlines()
        password = lines[-1]
        usernames = lines[1:5]
        return [{"username": x, "password": password} for x in usernames]

    def login(self, username, password):
        if self.driver.current_url != self.url:
            self.driver.get(self.url)
        self.driver.find_element(*(self.username_field)).send_keys(username)
        self.driver.find_element(*(self.password_field)).send_keys(password)
        self.driver.find_element(*(self.login_button)).click()
        return InventoryPage(self.driver)