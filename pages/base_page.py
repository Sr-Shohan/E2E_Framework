from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def set_value_into_element(self, locator, text, locator_initialization=False):
        if locator_initialization:
            locator = (By.XPATH, locator)
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator),
                                             "Web element was not available within the specific time out. "
                                             "Locator: '" + str(locator) + "'")
        self.clear_field(locator)
        self.wait_for_presence_of_element(locator).send_keys(text)

    def clear_field(self, locator):
        self.wait_for_presence_of_element(locator)

    def click_on_element(self, locator, locator_initialization=False, click_on_presence_of_element=False,
                         time_out=10):
        if locator_initialization:
            locator = (By.XPATH, locator)
        if click_on_presence_of_element:
            self.wait_for_presence_of_element(locator).click()
        else:
            WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                       "Web element was not available within the specific time out. "
                                                       "Locator: '" + str(locator) + "'")
            self.wait_for_element_to_be_clickable(locator).click()

    def wait_for_element_to_be_clickable(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.element_to_be_clickable(locator),
                                                          "Web element was not clickable within the specific time "
                                                          "out. Locator: '" + str(locator) + "'")

    def wait_for_presence_of_element(self, locator, time_out=10):
        return WebDriverWait(self.driver, time_out).until(EC.presence_of_element_located(locator),
                                                          "Web element was not present within the specific time "
                                                          "out. "
                                                          "Locator: '" + str(locator) + "'")
