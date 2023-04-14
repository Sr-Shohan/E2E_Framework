import time

import pytest

from pages.login.login import login


@pytest.mark.allure
def test_google_search(driver):
    # Create a new instance of the login page
    login_page = login(driver)
    # Load the login page
    login_page.load()
    # Provide login information
    login_page.provide_login_info()
    print(driver.current_url)
    # Verify that the user has successfully logged
    assert "https://opensource-demo.orangehrmlive.com" in driver.current_url

