from selenium.webdriver.common.by import By


class LoginFormLocators:
    #locator using CssSelector
    user_name_locator = (By.CSS_SELECTOR, "input#user-name")
    password_locator = (By.CSS_SELECTOR, "input#password")
    login_locator = (By.CSS_SELECTOR, "input#login-button")


