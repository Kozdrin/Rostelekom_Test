import time
from base.auth_page import AuthPage, AuthRegistration
from base.locators import AuthLocators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest



#

@allure.feature('Проверка  Формы авторизации, после редизайна')
def test_auth_form_display_positive(web_driver):

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
    WebDriverWait(right_block, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_MENU))
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_PHONE))
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_MAIL))
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_LOGIN))
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_TAB_LS))
    WebDriverWait(right_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_PASS))

    # Проверка наличия необходимых элементов в правом блоке
    WebDriverWait(left_block, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_SLOGAN))
#
#
#
#
@allure.story("Проверка переключения таба при вводе телефона,емайл")
def test_tabchange(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    # Вводим номер телефона
    page.enter_phone("79962049394")
    time.sleep(5)
    # Вводим email
    page.enter_email("kozdrin2013@yandex.ru")
    time.sleep(5)
    web_driver.find_element(*AuthLocators.AUTH_PASS).click()
    time.sleep(5)
    # Проверяем, что таб "Почта" выбран
    assert 'rt-tab--active' in web_driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-mail').get_attribute('class')
    page.enter_login("lk_67852809")
    time.sleep(5)
    web_driver.find_element(*AuthLocators.AUTH_PASS).click()
    time.sleep(5)
    # Проверяем, что таб "Почта" выбран
    assert 'rt-tab--active' in web_driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-login').get_attribute('class')
    page.enter_ls("596016237412")
    time.sleep(5)
    web_driver.find_element(*AuthLocators.AUTH_PASS).click()
    time.sleep(5)
    # Проверяем, что таб "Почта" выбран
    assert 'rt-tab--active' in web_driver.find_element(By.CSS_SELECTOR, '#t-btn-tab-ls').get_attribute('class')
    web_driver.delete_all_cookies()







@allure.story("Проверка авторизации по номеру телефона с некорректным номером.")
@pytest.mark.parametrize('phone, password', [
    ('79888778787', 'Kozdrin362425'),
])
def test_login_by_phone_incorrect_phone(web_driver, phone, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод некорректного номера телефона
    page.enter_phone(phone)
    # Ввод пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()



@allure.story("Проверка авторизации по номеру телефона с некорректным паролем.")
@pytest.mark.parametrize('phone, password', [
    ('79962049394', '123456'),
])
def test_login_by_phone_incorrect_password(web_driver, phone, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод номера телефона
    page.enter_phone(phone)
    # Ввод некорректного пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()




@allure.story("Проверка авторизации по почте с корректной почтой и паролем.")
@pytest.mark.parametrize('email, password', [
    ('kozdrin2013@yandex.ru', 'Kozdrin362425'),
])
def test_login_by_email(web_driver, email, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод почты
    page.enter_email(email)
    # Ввод пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Ожидание пока произойдет авторизация
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))

    # Проверка что авторизация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'
    web_driver.delete_all_cookies()




@allure.story("Проверка авторизации по почте с некорректной почтой.")
@pytest.mark.parametrize('email, password', [
    ('kozdrinroman@gmail', 'Kozdrin23805'),
])
def test_login_by_email_incorrect_email(web_driver, email, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод некорректной почты
    page.enter_email(email)
    # Ввод пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()



@allure.story("Проверка авторизации по почте с некорректным паролем.")
@pytest.mark.parametrize('email, password', [
    ('kozdrin2013@yandex.ru', '123456'),
])
def test_login_by_email_incorrect_password(web_driver, email, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод почты
    page.enter_email(email)
    # Ввод некорректного пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()



@allure.story("Проверка авторизации по логину с корректным логином и паролем.")
@pytest.mark.parametrize('login, password', [
    ('lk_67852809', 'Kozdrin362425'),
])
def test_login_by_login(web_driver, login, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод логина
    page.enter_login(login)
    # Ввод пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    # Ожидание пока произойдет авторизация
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))

    # Проверка что авторизация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'
    web_driver.delete_all_cookies()


@allure.story("Проверка авторизации по логину с некорректным логином.")
@pytest.mark.parametrize('login, password', [
    ('lk_46666809', 'Kozdrin362425'),
])
def test_login_by_login_incorrect_login(web_driver, login, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод некорректного логина
    page.enter_login(login)
    # Ввод пароля
    page.enter_pass(password)
    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()



@allure.story("Проверка авторизации по логину с некорректным паролем.")
@pytest.mark.parametrize('login, password', [
    ('lk_67852809', '123456'),
])
def test_login_by_login_incorrect_password(web_driver, login, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
        # Ввод логина
    page.enter_login(login)

    # Ввод некорректного пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))
    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()


@allure.story("Проверка авторизации по лицевому счету с некорректным лицевым счетом.")
@pytest.mark.parametrize('ls, password', [
    ('596016237542', 'Kozdrin362425'),
])
def test_login_by_ls_incorrect_ls(web_driver, ls, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    # Ввод некорректного лицевого счета
    page.enter_ls(ls)

    # Ввод пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD))

    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()




@allure.story("Проверка авторизации по лицевому счету с некорректным паролем.")
@pytest.mark.parametrize('ls, password', [
    ('596016237412', '123456'),
])
def test_login_by_ls_incorrect_password(web_driver, ls, password):
    page = AuthPage(web_driver)
    page.login_and_logout()


    # Ввод лицевого счета
    page.enter_ls(ls)

    # Ввод некорректного пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Проверка что авторизация не прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_INCORREKT_LOGIN_OR_PASSWORD).text == 'Неверный логин или пароль'
    web_driver.delete_all_cookies()



@allure.story("Проверка авторизации по лицевому счету с корректным лицевым счетом и паролем.")
@pytest.mark.parametrize('ls, password', [
    ('596016237412', 'Kozdrin362425'),
])
def test_login_by_ls(web_driver, ls, password):
    page = AuthPage(web_driver)
    page.login_and_logout()
    page.btn_ls()

    # Ввод лицевого счета
    page.enter_ls(ls)

    # Ввод пароля
    page.enter_pass(password)

    # Нажатие кнопки "Войти"
    page.btn_click()

    # Ожидание пока произойдет авторизация
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))

    # Проверка что авторизация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'
    web_driver.delete_all_cookies()
#
@allure.story("Проверка отображения ошибки при некорректном вводе номера телефона, почты, логина или лицевого счета.")
@pytest.mark.parametrize('phone, email, login, ls', [
    ('1234567890', None, None, None),
    (None, 'kozdrinromangmail', None, None),
    (None, None, 'Kozdrin1', None),
    (None, None, None, '59601620002'),
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
#

@allure.story("Проверка  элемента 'Забыл пароль' и ввода данных для восстановления пароля по телефону.")
@pytest.mark.parametrize('phone', [
    ('79962049394'),
])
def test_forgot_password_link_displayed(web_driver, phone):
    page = AuthPage(web_driver)
    page.login_and_logout()
    page.btn_forg_pass()
       # Ввод  номера телефона
    page.enter_phone(phone)

    # Проверка что отображается элемент "Забыл пароль"
    assert web_driver.find_element(*AuthLocators.Auth_FORGOTPASS_TEXT).text == 'Восстановление пароля'
    web_driver.delete_all_cookies()


#
@allure.story("Проверка отображения продуктового слогана ЛК 'Личный кабинет'.")
def test_product_slogan_displayed(web_driver):
    page = AuthPage(web_driver)
    page.open_auth_page()
    slogan_element = web_driver.find_element(*AuthLocators.AUTH_SLOGAN)
    print(slogan_element.text)

    # Проверка что отображается продуктовый слоган ЛК "Ростелеком ID"
    assert 'Личный кабинет' in web_driver.find_element(*AuthLocators.AUTH_SLOGAN).text
    web_driver.delete_all_cookies()


#
@allure.story("Проверка регистрации нового пользователя.")
@pytest.mark.parametrize('name,last_name, phone, password, city', [
    ('Иван','Иванов', '79962049384', 'Pass123456', 'Саратовская обл'),
])
def test_new_user_registration(web_driver, name, last_name, phone, password, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

    # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password)
    page.enter_pass_reg_conform(password)
    page.register_button()

    # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_REGISTRATION_CONFIRM_EMAIL))

    # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_CONFIRM_EMAIL).text == 'Подтверждение телефона'
    web_driver.delete_all_cookies()

@allure.story("Регистрация пользователя с занятым номером телефона")
@pytest.mark.parametrize('name,last_name, phone, password, city', [
('Иван', 'Иванов', '79962049394', 'Pass123456', 'Саратовская обл'),
])
def test_new_user_registration_same_number(web_driver, name, last_name, phone, password, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

        # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password)
    page.enter_pass_reg_conform(password)
    page.register_button()

        # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_REGISTRATION_ERR))

        # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_ERR).text == 'Учётная запись уже существует'
    web_driver.delete_all_cookies()

@allure.story("Регистрация пользователя 'Пароль должен содержать хотя бы одну заглваную букву'")
@pytest.mark.parametrize('name,last_name, phone, password, city', [
('Иван', 'Иванов', '79962032224', 'pass123456', 'Саратовская обл'),
])
def test_new_user_registration_Lit_attention(web_driver, name, last_name, phone, password, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

        # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password)
    page.enter_pass_reg_conform(password)


        # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_REGISTRATION_PASS_ATTENTHION_Lit))

        # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_PASS_ATTENTHION_Lit).text == 'Пароль должен содержать хотя бы одну заглавную букву'
    web_driver.delete_all_cookies()

@allure.story("Регистрация нового пользователя с коротким именем")
@pytest.mark.parametrize('name,last_name, phone, password, city', [
('И', 'Иванов', '79962032224', 'pass123456', 'Саратовская обл'),
])
def test_new_user_registration_shot_name(web_driver, name, last_name, phone, password, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

        # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password)
    page.enter_pass_reg_conform(password)


        # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_REGISTRATION_INPUT_NAME_ATTENTION))

        # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REGISTRATION_INPUT_NAME_ATTENTION).text == 'Необходимо заполнить поле кириллицей. От 2 до 30 символов.'
    web_driver.delete_all_cookies()

@allure.story("Регистрация пользователя c коротким паролем")
@pytest.mark.parametrize('name,last_name, phone, password, city', [
('Иван', 'Иванов', '79962032224', 'Pas6', 'Саратовская обл'),
])
def test_new_user_registration_pass_length(web_driver, name, last_name, phone, password, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

        # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password)
    page.enter_pass_reg_conform(password)


        # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_REG_PASS_LENGTH))

        # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REG_PASS_LENGTH).text == 'Длина пароля должна быть не менее 8 символов'
    web_driver.delete_all_cookies()

@allure.story("Регистрация пользователя c несовпадающими паролями")
@pytest.mark.parametrize('name,last_name, phone, password1, password2, city', [
('Иван', 'Иванов', '79962032224', 'Password6', 'Password7', 'Саратовская обл'),
])
def test_new_user_registration_pass_not_same(web_driver, name, last_name, phone, password1, password2, city):
    page = AuthRegistration(web_driver)
    page.open_auth_page()

        # Нажатие кнопки "Зарегистрироваться"
    page.registration()

    page.enter_first_name(name)
    page.enter_last_name(last_name)
    page.enter_city(city)
    page.enter_email_or_phone(phone)
    page.enter_pass_reg(password1)
    page.enter_pass_reg_conform(password2)
    page.register_button()



        # Ожидание пока произойдет регистрация
    WebDriverWait(web_driver, 10).until(
        EC.visibility_of_element_located(AuthLocators.AUTH_REG_PASS_NOT_SAME))

        # Проверка что регистрация прошла успешно
    assert web_driver.find_element(*AuthLocators.AUTH_REG_PASS_NOT_SAME).text == 'Пароли не совпадают'
    web_driver.delete_all_cookies()


