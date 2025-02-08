from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator, time=15):
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    def send_keys_to_element(self, locator, text):
        element = self.find_element(locator)
        element.send_keys(text)

    def select_option(self, locator, text):
        element = self.find_element(locator)
        select = Select(element)
        select.select_by_visible_text(text)