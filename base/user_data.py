class UserData:
    valid_phone = "79962049394"
    valid_email = "kozdrin2013@yandex.ru"
    valid_password = "Kozdrin362425"
    valid_ls = "596016237412"
    valid_login = ""
    invalid_ls = "596013437412"
    invalid_phone = "1234567890"
    invalid_email = "invalid_email.com"
    invalid_password = "123"
    invalid_login = ""

    #

    #
    #
    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #     # Находим элемент изображения капчи
    #     captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #     # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    #     if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():
    #
    #         time.sleep(10)
    #
    #         # Находим элемент изображения капчи снова, так как после обновления страницы элемент может стать неактуальным
    #         captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #         captcha_image_url = captcha_image_element.get_attribute('src')
    #         page_url = web_driver.current_url  # URL текущей страницы
    #         captcha_text = page.solve_captcha(captcha_image_url, page_url)
    #
    #         # Находим элемент поля ввода капчи
    #         captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)
    #
    #         # Имитация ручного ввода капчи
    #         for char in captcha_text:
    #             captcha_input_element.send_keys(char)
    #             time.sleep(random.uniform(0.1, 0.3))  # Задержка между символами
    #
    #         time.sleep(3)
    #
    #         # Нажимаем кнопку "Подтвердить"
    #         captcha_input_element.submit()
    #         time.sleep(3)
    #         page.enter_phone(phone)
    #         time.sleep(3)
    #         # Ввод пароля
    #         page.enter_pass(password)
    #         time.sleep(3)
    #
    #         # Нажатие кнопки "Войти"
    #         page.btn_click()
    #
    #     # Ожидание пока произойдет авторизация
    #     WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    #
    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем c капчей.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone_with_captcha(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #     max_captcha_attempts = 3
    #     for attempt in range(max_captcha_attempts):
    #         # Находим элемент изображения капчи
    #         captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #         # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    #         if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():
    #
    #             time.sleep(10)
    #
    #             # Находим элемент изображения капчи снова, так как после обновления страницы элемент может стать неактуальным
    #             captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #             captcha_image_url = captcha_image_element.get_attribute('src')
    #             page_url = web_driver.current_url  # URL текущей страницы
    #             captcha_text = page.solve_captcha(captcha_image_url, page_url)
    #
    #             # Находим элемент поля ввода капчи
    #             captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)
    #
    #             # Перемещаем курсор к полю ввода капчи
    #             pyautogui.moveTo(captcha_input_element.location['x'] + 5, captcha_input_element.location['y'] + 5)
    #
    #             # Имитируем ручной ввод капчи
    #             for c in captcha_text:
    #                 pyautogui.press(c)
    #                 time.sleep(random.uniform(0.1, 0.3))  # Задержка между нажатиями клавиш
    #
    #             # Нажимаем кнопку "Подтвердить"
    #             captcha_input_element.submit()
    #
    #             # Ожидание пока произойдет авторизация или появится новая капча
    #             try:
    #                 WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #                 break
    #             except TimeoutException:
    #                 pass
    #     else:
    #         assert False, "Не удалось авторизоваться после {} попыток решения капчи".format(max_captcha_attempts)
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #         # Ожидание пока произойдет авторизация
    #     WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    # def test_login_by_phone(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #         # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #
    #     # Находим элемент изображения капчи
    #     captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #     # Получаем значение атрибута src изображения капчи
    #     captcha_image_url = captcha_image_element.get_attribute('src')
    #
    #     # Ожидаем, пока изображение капчи загрузится
    #     WebDriverWait(web_driver, 10).until(EC.presence_of_element_located(AuthLocators.AUTH_CAPTCHA_IMG))
    #
    #     # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    #     if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():
    #         page.refresh_captcha()
    #         page_url = web_driver.current_url  # URL текущей страницы
    #         captcha_text = page.solve_captcha(captcha_image_url, page_url)
    #
    #         # Находим элемент поля ввода капчи
    #         captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)
    #
    #         # Вводим текст капчи в поле ввода
    #         captcha_input_element.send_keys(captcha_text)
    #
    #         # # Нажимаем кнопку "Подтвердить"
    #         # captcha_input_element.submit()
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #         # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #     # Ожидание пока произойдет авторизация
    #     WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #     # Находим элемент изображения капчи
    #     captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #     # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    #     if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():
    #
    #         time.sleep(10)
    #
    #         # Находим элемент изображения капчи снова, так как после обновления страницы элемент может стать неактуальным
    #         captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #         captcha_image_url = captcha_image_element.get_attribute('src')
    #         page_url = web_driver.current_url  # URL текущей страницы
    #         captcha_text = page.solve_captcha(captcha_image_url, page_url)
    #
    #         # Находим элемент поля ввода капчи
    #         captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)
    #
    #         # Имитация ручного ввода капчи
    #         for char in captcha_text:
    #             captcha_input_element.send_keys(char)
    #             time.sleep(random.uniform(0.1, 0.3))  # Задержка между символами
    #
    #         time.sleep(3)
    #
    #         # Нажимаем кнопку "Подтвердить"
    #         captcha_input_element.submit()
    #         time.sleep(3)
    #         page.enter_phone(phone)
    #         time.sleep(3)
    #         # Ввод пароля
    #         page.enter_pass(password)
    #         time.sleep(3)
    #
    #         # Нажатие кнопки "Войти"
    #         page.btn_click()
    #
    #     # Ожидание пока произойдет авторизация
    #     WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    #
    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем c капчей.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone_with_captcha(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #     max_captcha_attempts = 3
    #     for attempt in range(max_captcha_attempts):
    #         # Находим элемент изображения капчи
    #         captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #         # Если изображение капчи отображается и доступно для взаимодействия, вызываем функцию для ее решения
    #         if captcha_image_element.is_displayed() and captcha_image_element.is_enabled():
    #
    #             time.sleep(10)
    #
    #             # Находим элемент изображения капчи снова, так как после обновления страницы элемент может стать неактуальным
    #             captcha_image_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_IMG)
    #
    #             captcha_image_url = captcha_image_element.get_attribute('src')
    #             page_url = web_driver.current_url  # URL текущей страницы
    #             captcha_text = page.solve_captcha(captcha_image_url, page_url)
    #
    #             # Находим элемент поля ввода капчи
    #             captcha_input_element = web_driver.find_element(*AuthLocators.AUTH_CAPTCHA_INPUT)
    #
    #             # Перемещаем курсор к полю ввода капчи
    #             pyautogui.moveTo(captcha_input_element.location['x'] + 5, captcha_input_element.location['y'] + 5)
    #
    #             # Имитируем ручной ввод капчи
    #             for c in captcha_text:
    #                 pyautogui.press(c)
    #                 time.sleep(random.uniform(0.1, 0.3))  # Задержка между нажатиями клавиш
    #
    #             # Нажимаем кнопку "Подтвердить"
    #             captcha_input_element.submit()
    #
    #             # Ожидание пока произойдет авторизация или появится новая капча
    #             try:
    #                 WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #                 break
    #             except TimeoutException:
    #                 pass
    #     else:
    #         assert False, "Не удалось авторизоваться после {} попыток решения капчи".format(max_captcha_attempts)
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'

    # @allure.story("Проверка авторизации по номеру телефона с корректным номером и паролем.")
    # @pytest.mark.parametrize('phone, password', [
    #     ('79962049394', 'Kozdrin23805'),
    # ])
    # def test_login_by_phone(web_driver, phone, password):
    #     page = AuthPage(web_driver)
    #     page.open_auth_page()
    #     # Ввод номера телефона
    #     page.enter_phone(phone)
    #     # Ввод пароля
    #     page.enter_pass(password)
    #
    #     # Нажатие кнопки "Войти"
    #     page.btn_click()
    #
    #         # Ожидание пока произойдет авторизация
    #     WebDriverWait(web_driver, 10).until(EC.visibility_of_element_located(AuthLocators.AUTH_USER_NAME))
    #
    #     # Проверка что авторизация прошла успешно
    #     assert web_driver.find_element(*AuthLocators.AUTH_USER_NAME).text == 'Коздринь\nРоман Романович'