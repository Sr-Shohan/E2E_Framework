from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from allure_commons._allure import attach
from allure_commons.types import AttachmentType


@pytest.fixture(scope="session", autouse=True)
def driver():
    # Set up the ChromeOptions object for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    # Initialize the WebDriver instance with the ChromeOptions object
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    # Return the WebDriver instance for use in the tests
    yield driver
    # Tear down the WebDriver instance
    driver.quit()


def allure_report(request):
    yield
    cmd = f"allure generate {request.config.rootdir}/allure-results --clean"
    import subprocess
    subprocess.call(cmd, shell=True)
    attach("Allure Report", open(f"{request.config.rootdir}/allure-report/index.html", "rb").read(),
           AttachmentType.HTML)


@pytest.fixture
def screenshot_on_failure(request, driver):
    yield
    if request.node.rep_call.failed:
        # Take a screenshot of the current browser window
        screenshot = driver.get_screenshot_as_png()
        # Attach the screenshot to the Allure report
        attach(screenshot, name="Screenshot", attachment_type=AttachmentType.PNG)
