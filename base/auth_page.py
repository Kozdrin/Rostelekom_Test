import requests

import base64

from selenium.webdriver.common.keys import Keys
from base.base_page import BasePage
from base.locators import AuthLocators
import time
import allure

class AuthPage(BasePage):

    def __init__(self, driver, url="https://b2c.passport.rt.ru/auth"):
        self.driver = driver
        self.url = url
        super().__init__(self.driver, url=self.url)

    @allure.step("Ввод email")
    def enter_email(self, value):
        email_input = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)

        # Очищаем поле ввода, если оно заполнено
        if email_input.get_attribute("value"):
            email_input.send_keys(Keys.BACK_SPACE * len(email_input.get_attribute("value")))
            assert not email_input.get_attribute("value"), "Поле ввода не очищено"

        email_input.send_keys(value)
        return email_input

    @allure.step("Ввод телефона")
    def enter_phone(self, value):
        phone_input = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)

        # Очищаем поле ввода, если оно заполнено
        if phone_input.get_attribute("value"):
            phone_input.send_keys(Keys.BACK_SPACE * len(phone_input.get_attribute("value")))
            assert not phone_input.get_attribute("value"), "Поле ввода не очищено"

        phone_input.send_keys(value)
        return phone_input

    @allure.step("Ввод пароля")
    def enter_pass(self, value):
        password = self.driver.find_element(*AuthLocators.AUTH_PASS)
        password.send_keys(value)
        if password.get_attribute("value"):
            password.send_keys(Keys.BACK_SPACE * len(password.get_attribute("value")))
            assert not password.get_attribute("value"), "Поле ввода не очищено"

        password.send_keys(value)
        return password

    @allure.step("Подтверждение пароля")
    def enter_pass_confirm(self, value):
        pass_confirm = self.driver.find_element(*AuthLocators.AUTH_PASS_CONFIRM)
        pass_confirm.send_keys(value)

    @allure.step("Ввод логина")
    def enter_login(self,value):
        login = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)

        if login.get_attribute("value"):
            login.send_keys(Keys.BACK_SPACE * len(login.get_attribute("value")))
            assert not login.get_attribute("value"), "Поле ввода не очищено"

        login.send_keys(value)
        return login

    @allure.step("Ввод лицевого счета")
    def enter_ls(self, value):
        ls = self.driver.find_element(*AuthLocators.AUTH_EMAIL_PHONE_NUMBER)
        ls.send_keys(value)
        if ls.get_attribute("value"):
            ls.send_keys(Keys.BACK_SPACE * len(ls.get_attribute("value")))
            assert not ls.get_attribute("value"), "Поле ввода не очищено"

        ls.send_keys(value)
        return ls

    @allure.step("Нажатие кнопки")
    def btn_click(self):
        btn = self.driver.find_element(*AuthLocators.AUTH_BTN)
        btn.click()
        time.sleep(3)  # ждем реакции

    @allure.step("Открытие страницы авторизации")
    def open_auth_page(self):
        self.open_page(self.url)



    @allure.step("Переход на ссылку лицевый счет")
    def btn_ls(self):
        btn_ls = self.driver.find_element(*AuthLocators.AUTH_TAB_LS)
        btn_ls.click()
    @allure.step("Переход по кнопке забыли пароль")
    def btn_forg_pass(self):
        btn_forg_pass = self.driver.find_element(*AuthLocators.AUTH_TAB_FORGOTT_PASS)
        btn_forg_pass.click()

    @allure.step("Нажатие кнопки продолжить при восстановлении пароля")
    def btn_forg_pass_next(self):
        btn_forg_pass_next = self.driver.find_element(*AuthLocators.AUTH_BTN_FORG_PASS_NEXT)
        btn_forg_pass_next.click()

    @allure.step("Нажатие кнопки авторизация по временному коду")
    def btn_temp_code(self):
        btn_temp_code = self.driver.find_element(*AuthLocators.AUTH_TAB_TEMP_CODE)
        btn_temp_code.click()






    def exit_lk(self):
        logout = self.driver.find_element(*AuthLocators.AUTH_EXIT)
        time.sleep(1)
        logout.click()
        time.sleep(1)

    @allure.step("Авторизация и выход перед тестом с некорректными данными")
    def login_and_logout(self):
        self.open_auth_page()

        # Ввод номера телефона
        self.enter_phone("79962049394")

        # Ввод пароля
        self.enter_pass("Kozdrin362425")

        # Нажатие кнопки "Войти"
        self.btn_click()
        time.sleep(5)

        # Выход из аккаунта
        self.exit_lk()

    @allure.step("Обновление капчи")
    def refresh_captcha(self):
        refresh_captcha_button = self.driver.find_element(*AuthLocators.AUTH_REFRESH_CAPTCHA)
        refresh_captcha_button.click()

    @allure.step("Решение капчи")
    def solve_captcha(self, captcha_image_url, page_url):
        """
        Решает капчу с помощью сервиса Anti-Captcha.
        :param captcha_image_url: Ссылка на изображение капчи.
        :param page_url: URL текущей страницы.
        :return: Текст, введенный в капчу.
        """
        api_key = "4b6a9a2bcd6e8f12b0dc0f8f698fa018"

        # Отправляем запрос на распознавание капчи
        with requests.Session() as session:
            response = session.get(captcha_image_url)
            response.raise_for_status()

            with open("captcha.png", "wb") as file:
                file.write(response.content)

            captcha_files = {"file": open("captcha.png", "rb")}
            captcha_data = {
                "clientKey": api_key,
                "task": {
                    "type": "ImageToTextTask",
                    "body": base64.b64encode(response.content).decode(),
                    "phrase": 0,
                    "case": 0,
                    "numeric": 0,
                    "math": 0,
                    "minLength": 0,
                    "maxLength": 0,
                    "language": "eng",
                    "softId": 0,
                    "method": "base64",
                    "regions": [],
                    "lines": [],
                    "url": page_url,
                },
            }
            captcha_url = "https://api.anti-captcha.com/createTask"
            print(f"Sending request to {captcha_url}\nData: {captcha_data}\nFiles: {captcha_files}")
            response = session.post(captcha_url, json=captcha_data)
            print(f"Received response with status code {response.status_code}\nContent: {response.json()}")

            response.raise_for_status()

            captcha_id = response.json().get("taskId")
            if not captcha_id:
                raise Exception("Не удалось получить ID капчи")

        # Ожидаем, пока капча будет распознана
        time.sleep(10)

        # Получаем результат распознавания капчи
        with requests.Session() as session:
            captcha_data = {"clientKey": api_key, "taskId": captcha_id}
            captcha_url = "https://api.anti-captcha.com/getTaskResult"
            response = session.post(captcha_url, json=captcha_data)
            response.raise_for_status()

            captcha_text = response.json().get("solution", {}).get("text")
            if not captcha_text:
                raise Exception("Не удалось распознать капчу")

        return captcha_text

class AuthRegistration(AuthPage):

    def __init__(self, driver,
                 url="https://b2c.passport.rt.ru/auth"):
        self.driver = driver
        self.url = url
        super().__init__(self.driver, url=self.url)

    @allure.step("Ввод города")
    def enter_city(self, value):
        city = self.driver.find_element(*AuthLocators.AUTH_CITY)
        if city.get_attribute("value"):
            city.send_keys(Keys.BACK_SPACE * len(city.get_attribute("value")))
            assert not city.get_attribute("value"), "Поле ввода не очищено"
        city.send_keys(value)
        time.sleep(3)

    @allure.step("Ввод пароля")
    def enter_pass_reg(self, value):
        reg_pass = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION_PASS)
        reg_pass.send_keys(value)
        time.sleep(3)

    @allure.step("Подтверждение пароля")
    def enter_pass_reg_conform(self, value):
        reg_pass_confirm = self.driver.find_element(*AuthLocators.AUTH_PASS_CONFIRM)
        reg_pass_confirm.send_keys(value)
        time.sleep(3)


    @allure.step("Ввод имени")
    def enter_first_name(self, value):
        first_name = self.driver.find_element(*AuthLocators.AUTH_FIRST_NAME)
        first_name.send_keys(value)
        time.sleep(3)

    @allure.step("Ввод фамилии")
    def enter_last_name(self, value):
        second_name = self.driver.find_element(*AuthLocators.AUTH_LAST_NAME)
        second_name.send_keys(value)
        time.sleep(3)

    @allure.step("Ввод email или телефона")
    def enter_email_or_phone(self, value):
        email_or_phone = self.driver.find_element(*AuthLocators.AUTH_EMAIL_OR_PHONE)
        email_or_phone.send_keys(value)
        time.sleep(3)

    @allure.step("Регистрация")
    def registration(self):
        enter = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION)
        enter.click()
        time.sleep(3)

    @allure.step("Нажатие кнопки регистрации")
    def register_button(self):
        btn_registr = self.driver.find_element(*AuthLocators.AUTH_REGISTRATION_BTN)
        btn_registr.click()
        time.sleep(2)

