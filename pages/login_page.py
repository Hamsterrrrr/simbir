import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    LOGIN_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    CUSTOMER_LOGIN_BUTTON = (By.CSS_SELECTOR, "button[ng-click='customer()']")
    CUSTOMER_DROPDOWN = (By.ID, "userSelect")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    
    @allure.step("Login as {customer_name}")
    def login_as_customer(self, customer_name):
        self.open(self.LOGIN_URL)
        self.click_element(self.CUSTOMER_LOGIN_BUTTON)
        self.select_option(self.CUSTOMER_DROPDOWN, customer_name)
        self.click_element(self.LOGIN_BUTTON)