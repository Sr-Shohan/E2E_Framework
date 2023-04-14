from selenium.webdriver.common.by import By


class LoginFormLocators:
    #locator using CssSelector
    user_name_locator = (By.CSS_SELECTOR, "input[name='username']")
    password_locator = (By.CSS_SELECTOR, 'input[name="password"]')
    login_button_locator = (By.CSS_SELECTOR, "button[type='submit']")


