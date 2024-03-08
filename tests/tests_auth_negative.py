import time
from base.auth_page import AuthPage, AuthRegistration
from base.locators import AuthLocators
import allure

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import random

@allure.feature('Проверка  Формы авторизации, согласно требованиям заказчика')
def test_auth_form_display_negative(web_driver):

    page = AuthPage(web_driver)
    page.open_auth_page()


    assert WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_MAIN))

    # Проверка разделения формы на два блока"
    left_block = web_driver.find_element(*AuthLocators.AUTH_LEFT_BLOCK)
    right_block = web_driver.find_element(*AuthLocators.AUTH_RIGHT_BLOCK)
    assert left_block.is_displayed() and right_block.is_displayed()

    # Проверка наличия необходимых элементов в левом блоке
    #Меню выбора типа аутентификации
    # Проверка наличия необходимых элементов в левом блоке
    WebDriverWait(left_block, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_MENU))
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_PHONE))
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_MAIL))
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_LOGIN))
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_LS))
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_PASS))

    # Проверка наличия необходимых элементов в правом блоке
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_SLOGAN))

@allure.story("Преверка функцмонирования службы безопасности сайта, автоматизированный ввод капчи")
@pytest.mark.parametrize('phone, password', [
    ('79962049394', 'Kozdrin362425'),
])
def test_login_by_phone(web_driver, phone, password):
    page = AuthPage(web_driver)
    page.open_auth_page()
    # Ввод номера телефона
    page.enter_phone(phone)
    # Ввод пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Находим элемент изображения капчи
    captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)

    # Сохраняем изображение капчи до ввода кода
    captcha_image_before = captcha_image_element.screenshot_as_png

    # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():

        time.sleep(10)

        # Находим элемент изображения капчи снова, так как после обновления страницы элемент может стать неактуальным
        captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)

        captcha_image_url = captcha_image_element.get_attribute('src')
        page_url = web_driver.current_url  # URL текущей страницы
        captcha_text = page.solve_captcha(captcha_image_url, page_url)

        # Находим элемент поля ввода капчи
        captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)

        # Имитация ручного ввода капчи
        for char in captcha_text:
            captcha_input_element.send_keys(char)
            time.sleep(random.uniform(0.1, 0.3))  # Задержка между символами

        time.sleep(3)

        # Нажимаем кнопку "Подтвердить"
        captcha_input_element.submit()
        # Ожидание пока произойдет перезагрузка страницы
        WebDriverWait(web_driver, 10).until(EC.staleness_of(captcha_image_element))

        # Находим элемент изображения капчи снова
        captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
        time.sleep(3)
        page.enter_phone(phone)
        time.sleep(3)
        # Ввод пароля
        page.enter_pass(password)
        time.sleep(3)

        # Нажатие кнопки "Войти"
        page.btn_click()


    # Сохраняем изображение капчи после ввода кода
    captcha_image_after = captcha_image_element.screenshot_as_png

    # Сравниваем изображения капчи до и после ввода кода
    assert captcha_image_before != captcha_image_after, "Картинка капчи не изменилась после ввода кода"


@allure.story("Проверка отображения продуктового слогана ЛК 'Ростелеком ID'.")
def test_product_slogan_displayed2(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    slogan_element = web_driver.find_element(*AuthLocators.AUTH_SLOGAN)
    print(slogan_element.text)

    # Проверка что отображается продуктовый слоган ЛК "Ростелеком ID"
    assert 'Ростелеком ID' in web_driver.find_element(*AuthLocators.AUTH_SLOGAN).text
    web_driver.delete_all_cookies()


@allure.story("Проверка перенаправления на страницу redirect_uri после успешной авторизации.")
@pytest.mark.parametrize('phone, password', [
    ('79962049394', 'Kozdrin362425'),
])
def test_redirect_to_redirect_uri(web_driver, phone, password):
    page = AuthPage(web_driver)
    page.open_auth_page()

    # Ввод номера телефона
    page.enter_phone(phone)

    # Ввод пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Ожидание пока произойдет авторизация
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))

    # Проверка что произошло перенаправление на страницу redirect_uri
    assert web_driver.current_url == 'https://start.rt.ru/?tab=main'
    web_driver.delete_all_cookies()

@allure.story("Проверка отображения ошибки при некорректном вводе номера телефона, почты, логина или лицевого счета.")
@pytest.mark.parametrize('phone, email, login, ls', [
    ('1234567890', None, None, None),
    (None, 'kozdrinroman@gmail', None, None),
    (None, None, 'Kozdrin1', None),
    (None, None, None, '123456789'),
])
def test_error_message_displayed(web_driver, phone, email, login, ls):
    page = AuthPage(web_driver)
    page.open_auth_page()

    # Ввод некорректных данных
    if phone:
        page.enter_phone(phone)
    if email:
        page.enter_email(email)
    if login:
        page.enter_login(login)
    if ls:
        page.enter_ls(ls)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Проверка что отображается сообщение об ошибке
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()

@allure.story("Проверка возможности авторизации по временному коду.")
@pytest.mark.parametrize('phone', [
    ('79962049394'),
])
def test_login_by_temporary_code(web_driver, phone):

    page = AuthPage(web_driver)
    page.open_auth_page()


    # Нажатие кнопки "войти по временному коду"
    page.btn_temp_code()
    # Ввод номера телефона
    page.enter_phone(phone)

    # Проверка отображения названия сервиса "Авторизация по коду"
    assert web_driver.find_element(*AuthLocators.AUTH_TEMP_CODE_TEXT).text == 'Авторизация по коду'
    web_driver.delete_all_cookies()
