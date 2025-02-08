import allure
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TransactionsPage(BasePage):
    TRANSACTIONS_BUTTON = (By.CSS_SELECTOR, "button[ng-click='transactions()']")
    TRANSACTIONS_TABLE = (By.CSS_SELECTOR, "table.table-bordered.table-striped")
    FIRST_ROW = (By.ID, "anchor0")
    
    @allure.step("Open transactions page")
    def open_transactions(self):
        self.click_element(self.TRANSACTIONS_BUTTON)
        
    @allure.step("Get all transactions")
    def get_all_transactions(self):
        self.find_element(self.FIRST_ROW)
        transactions = []
        table = self.find_element(self.TRANSACTIONS_TABLE)
        rows = table.find_elements(By.TAG_NAME, "tr")[1:]
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, "td")
            date = cols[0].text
            amount = float(cols[1].text)
            transaction_type = cols[2].text
            transactions.append((date, amount, transaction_type))
        return transactions