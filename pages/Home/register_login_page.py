from locator.login_form_locators import LoginFormLocators
from locator.Register_login_form_locator import RegisterLoginForm
from pages.base_page import BasePage


class RegisterLogin(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def provide_initial_register_info(self, register_data):
        self.set_value_into_element(RegisterLoginForm.register_name_locator,
                                    register_data['registration']['name'])
        self.set_value_into_element(RegisterLoginForm.register_email_locator, register_data['registration']['email'])
        self.click_on_element(RegisterLoginForm.register_submit_button_locator)

