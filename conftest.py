from selenium import webdriver
import pytest


@pytest.fixture(scope="module")
def browser():
    # Initialize the WebDriver instance
    driver = webdriver.Chrome()

    # Return the driver instance to the test module
    yield driver

    # Close the driver instance when the test is complete
    driver.quit()
