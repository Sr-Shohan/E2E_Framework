import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from locator.login_form_locators import LoginFormLocators
from pages.base_page import BasePage


class login(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def provide_login_info(self, ):
        self.set_value_into_element(LoginFormLocators.user_name_locator, "Admin")
        self.set_value_into_element(LoginFormLocators.password_locator, "admin123")
        self.click_on_element(LoginFormLocators.login_button_locator)

    def load(self):
        self.driver.get('https://opensource-demo.orangehrmlive.com')


