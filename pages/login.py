import time

from selenium.webdriver.common.by import By
from locator.login_form_locators import LoginFormLocators

class GoogleHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.username_locator = LoginFormLocators.user_name_locator
        self.password_locator = LoginFormLocators.password_locator
        self.login_locator = LoginFormLocators.login_locator

    def load(self):
        self.driver.get("https://www.saucedemo.com/")

    def provide_login_info(self, username, password):
        # Find the username and password fields and input the provided values
        self.driver.find_element(*self.username_locator).send_keys(username)
        self.driver.find_element(*self.password_locator).send_keys(password)
        self.driver.find_element(*self.login_locator).click()
