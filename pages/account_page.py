import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class AccountPage(BasePage):
    DEPOSIT_BUTTON = (By.CSS_SELECTOR, "button[ng-click='deposit()']")
    AMOUNT_DEPOSIT = (By.CSS_SELECTOR, "input[ng-model='amount']")
    APPROVE_DEPOSIT = (By.CSS_SELECTOR, "button[class='btn btn-default']")
    WITHDRAWL_BUTTON = (By.CSS_SELECTOR, "button[ng-click='withdrawl()']")
    APPROVE_WITHDRAW = (By.CSS_SELECTOR, "button[class='btn btn-default']")
    BALANCE_ELEMENT = (By.CSS_SELECTOR, "div.center strong:nth-child(2)")
    APPROVE_SUCCESS = (By.CSS_SELECTOR, "span[ng-show='message']")
    WITHDRAWL_LABEL = (By.XPATH, "//label[contains(text(), 'Amount to be Withdrawn :')]")

    @allure.step("Enter deposit amount: {amount}")
    def submit_deposit(self, amount):
        self.click_element(self.DEPOSIT_BUTTON)
        self.send_keys_to_element(self.AMOUNT_DEPOSIT, amount)
        self.click_element(self.APPROVE_DEPOSIT)
        success_message = self.find_element(self.APPROVE_SUCCESS).text
        return success_message

    @allure.step("Enter withdrawl amount: {amount}")
    def enter_withdrawl(self, amount):
        self.click_element(self.WITHDRAWL_BUTTON)
        self.find_element(self.WITHDRAWL_LABEL)
        self.send_keys_to_element(self.AMOUNT_DEPOSIT, amount)
        self.click_element(self.APPROVE_WITHDRAW)

        success_message = self.find_element(self.APPROVE_SUCCESS).text
        return success_message
    
    def get_balance(self):
        balance = self.find_element(self.BALANCE_ELEMENT).text
        return int(balance)
