import time

import pytest

from pages.login import GoogleHomePage


@pytest.mark.allure
def test_google_search(driver, screenshot_on_failure):
    # Create a new instance of the login page
    login_page = GoogleHomePage(driver)
    # Load the login page
    login_page.load()
    # Provide login information
    login_page.provide_login_info("standard_userr", "secret_sauce")
    # Verify that the user has successfully logged
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    time.sleep(3)
