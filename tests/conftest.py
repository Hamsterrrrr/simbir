import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

@pytest.fixture(scope="module")
def setup():
    selenium_host = os.environ.get("SELENIUM_HOST", "localhost")
    selenium_port = os.environ.get("SELENIUM_PORT", "4444")
    selenium_url = f"http://{selenium_host}:{selenium_port}/wd/hub"
    
    # Настройка для Firefox
    options = Options()
    
    # Настройка WebDriver для Selenium Grid
    driver = webdriver.Remote(
        command_executor=selenium_url,
        options=options
    )
    driver.maximize_window()
    yield driver
    driver.quit()