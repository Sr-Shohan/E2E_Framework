from locator.login_form_locators import LoginFormLocators
from pages.base_page import BasePage


class homepage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def load_URL(self):
        self.driver.get('http://automationexercise.com')

    def add_cart_item(self):
        self.click_on_element(LoginFormLocators.add_cart_initial_locator)
        self.click_on_element(LoginFormLocators.add_cart_locator)
        self.click_on_element(LoginFormLocators.modal_cart_locator)
