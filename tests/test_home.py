from pages.home.home import GoogleHomePage
from selenium import webdriver
def test_google_search(browser):
    # Create a new instance of the Google home page
    home_page = GoogleHomePage(browser)

    # Load the Google home page
    home_page.load()

    # Search for a query
    home_page.search_for("Selenium with Python")

    # Verify that the search results page title contains the query
    assert "Selenium with Python" in browser.title