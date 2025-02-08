import allure
import pandas as pd
from datetime import datetime
import pytest
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transactions_page import TransactionsPage

@allure.feature("Banking Operations")
class TestBanking:
    @pytest.fixture(autouse=True)
    def setup_class(self, setup):
        """
        Фикстура для инициализации драйвера и страниц.
        """
        self.driver = setup
        self.login_page = LoginPage(self.driver)
        self.account_page = AccountPage(self.driver)
        self.transactions_page = TransactionsPage(self.driver)

    @allure.story("Deposit, Withdraw, and Check Transactions")
    def test_banking_operations(self):
        """
        Тест для проверки операций: депозит, списание и проверка транзакций.
        """
        # Шаг 1: Авторизация пользователя "Harry Potter"
        with allure.step("Step 1: Авторизация пользователя 'Harry Potter'"):
            self.login_page.login_as_customer("Harry Potter")

        # Шаг 2: Вычисление числа Фибоначчи для текущего дня
        with allure.step("Step 2: Вычисление числа Фибоначчи для текущего дня"):
            def fibonacci(n): # такую штуку надо выносить но так как в тестовом я не переиспользую ее то получается не нарушаю DRY поэтому для простоты оставил тут
                a, b = 0, 1
                for _ in range(n):
                    a, b = b, a + b
                return a

            current_day = datetime.now().day + 1
            fib_number = fibonacci(current_day)
            allure.attach(str(fib_number), name="Fibonacci Number", attachment_type=allure.attachment_type.TEXT)

        # Шаг 3: Пополнение счета
        with allure.step("Step 3: Пополнение счета на сумму, равную числу Фибоначчи"):
            success_message = self.account_page.submit_deposit(fib_number)
            assert success_message == "Deposit Successful", f"Expected 'Deposit Successful', but got '{success_message}'"
            allure.attach(success_message, name="Deposit Message", attachment_type=allure.attachment_type.TEXT)

        # Шаг 4: Списание со счета
        with allure.step("Step 4: Списание со счета суммы, равной числу Фибоначчи"):
            success_message = self.account_page.enter_withdrawl(fib_number)
            assert success_message == "Transaction successful", f"Expected 'Transaction successful', but got '{success_message}'"
            allure.attach(success_message, name="Withdrawal Message", attachment_type=allure.attachment_type.TEXT)

        # Шаг 5: Проверка баланса
        with allure.step("Step 5: Проверка баланса после операций"):
            balance = self.account_page.get_balance()
            assert balance == 0, f"Balance to be 0, but got {balance}"
            allure.attach(str(balance), name="Final Balance", attachment_type=allure.attachment_type.TEXT)

        # Шаг 6: Проверка транзакций
        with allure.step("Step 6: Проверка списка транзакций"):
            self.transactions_page.open_transactions()
            transactions = self.transactions_page.get_all_transactions()
            allure.attach(str(transactions), name="Transactions List", attachment_type=allure.attachment_type.TEXT)

        # Шаг 7: Создание файла CSV
        with allure.step("Step 7: Создание файла CSV с транзакциями"):
            df = pd.DataFrame(transactions, columns=["Date", "Amount", "Type"])
            df.to_csv("transactions.csv", index=False)

        # Шаг 8: Интеграция Allure с CSV-файлом
        with allure.step("Step 8: Прикрепление файла CSV к отчету Allure"):
            with open("transactions.csv", "rb") as file:
                allure.attach(file.read(), name="transactions.csv", attachment_type=allure.attachment_type.CSV)