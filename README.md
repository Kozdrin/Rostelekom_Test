# Автоматизированные тесты проверки сервиса авторизации и регистрации "Ростелеком"
test_auth_form_display_positive - Проверка отображения формы авторизации, после редизайна. Тест проверяет, что все необходимые элементы формы авторизации отображаются корректно и разделены на два блока.

test_tabchange - Проверка переключения таба при вводе телефона, емайла. Тест проверяет, что при вводе номера телефона, email или логина, автоматически выбирается соответствующий таб.

test_login_by_phone_incorrect_phone - Проверка авторизации по номеру телефона с некорректным номером. Тест проверяет, что при вводе некорректного номера телефона, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_phone_incorrect_password - Проверка авторизации по номеру телефона с некорректным паролем. Тест проверяет, что при вводе некорректного пароля, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_email - Проверка авторизации по почте с корректной почтой и паролем. Тест проверяет, что при вводе корректной почты и пароля, авторизация проходит успешно и отображается имя пользователя.

test_login_by_email_incorrect_email - Проверка авторизации по почте с некорректной почтой. Тест проверяет, что при вводе некорректной почты, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_email_incorrect_password - Проверка авторизации по почте с некорректным паролем. Тест проверяет, что при вводе некорректного пароля, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_login - Проверка авторизации по логину с корректным логином и паролем. Тест проверяет, что при вводе корректного логина и пароля, авторизация проходит успешно и отображается имя пользователя.

test_login_by_login_incorrect_login - Проверка авторизации по логину с некорректным логином. Тест проверяет, что при вводе некорректного логина, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_login_incorrect_password - Проверка авторизации по логину с некорректным паролем. Тест проверяет, что при вводе некорректного пароля, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_ls_incorrect_ls - Проверка авторизации по лицевому счету с некорректным лицевым счетом. Тест проверяет, что при вводе некорректного лицевого счета, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_ls_incorrect_password - Проверка авторизации по лицевому счету с некорректным паролем. Тест проверяет, что при вводе некорректного пароля, авторизация не проходит и отображается сообщение об ошибке.

test_login_by_ls - Проверка авторизации по лицевому счету с корректным лицевым счетом и паролем. Тест проверяет, что при вводе корректного лицевого счета и пароля, авторизация проходит успешно и отображается имя пользователя.

test_error_message_displayed - Проверка отображения ошибки при некорректном вводе номера телефона, почты, логина или лицевого счета. Тест проверяет, что при вводе некорректных данных, отображается сообщение об ошибке.

test_forgot_password_link_displayed - Проверка элемента 'Забыл пароль' и ввода данных для восстановления пароля по телефону. Тест проверяет, что при нажатии на кнопку "Забыл пароль", отображается форма для восстановления пароля по телефону.

test_product_slogan_displayed - Проверка отображения продуктового слогана ЛК 'Личный кабинет'. Тест проверяет, что продуктовый слоган ЛК "Личный кабинет" отображается корректно.

test_new_user_registration - Проверка регистрации нового пользователя. Тест проверяет, что при вводе корректных данных, регистрация проходит успешно и отображается сообщение об успешной регистрации.

test_new_user_registration_same_number - Регистрация пользователя с занятым номером телефона. Тест проверяет, что при попытке зарегистрироваться с занятым номером телефона, отображается сообщение об ошибке.

test_new_user_registration_Lit_attention - Регистрация пользователя 'Пароль должен содержать хотя бы одну заглавную букву'. Тест проверяет, что при регистрации пользователя с паролем, не содержащим заглавных букв, отображается сообщение об ошибке.

test_new_user_registration_shot_name - Регистрация нового пользователя с коротким именем. Тест проверяет, что при регистрации пользователя с именем, короче двух символов, отображается сообщение об ошибке.

test_new_user_registration_pass_length - Регистрация пользователя c коротким паролем. Тест проверяет, что при регистрации пользователя с паролем, короче восьми символов, отображается сообщение об ошибке.

test_new_user_registration_pass_not_same - Регистрация пользователя c несовпадающими паролями. Тест проверяет, что при регистрации пользователя с несовпадающими паролями, отображается сообщение об ошибке.

test_auth_form_display_negative - Проверяет, что форма авторизации отображается корректно и содержит необходимые элементы. 

test_captcha_functionality - Проверяет функционирование службы безопасности сайта, автоматизированный ввод капчи. 

test_product_slogan_displayed - Проверяет, что отображается продуктовый слоган ЛК 'Ростелеком ID'. 

test_redirect_to_redirect_uri - Проверяет, что после успешной авторизации происходит перенаправление на страницу redirect_uri. 

test_error_message_displayed - Проверяет, что при некорректном вводе номера телефона, почты, логина или лицевого счета, отображается соответствующее сообщение об ошибке. 

test_temporary_code_authorization - Проверяет, что авторизация по временному коду проходит успешно. 




Команды для запусков тестов


pytest -v tests/test_auth_page.py::test_auth_form_display_positive --alluredir allure-results

pytest -v tests/test_auth_page.py::test_tabchange --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_phone_incorrect_phone --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_phone_incorrect_password --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_email --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_email_incorrect_email --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_email_incorrect_password --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_login --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_login_incorrect_login --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_login_incorrect_password --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_ls_incorrect_ls --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_ls_incorrect_password --alluredir allure-results

pytest -v tests/test_auth_page.py::test_login_by_ls --alluredir allure-results

pytest -v tests/test_auth_page.py::test_error_message_displayed --alluredir allure-results

pytest -v tests/test_auth_page.py::test_forgot_password_link_displayed --alluredir allure-results

pytest -v tests/test_auth_page.py::test_product_slogan_displayed --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration_same_number --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration_Lit_attention --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration_shot_name --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration_pass_length --alluredir allure-results

pytest -v tests/test_auth_page.py::test_new_user_registration_pass_not_same --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_auth_form_display_negative --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_captcha_functionality --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_product_slogan_displayed --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_redirect_to_redirect_uri --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_error_message_displayed --alluredir allure-results

pytest -v tests/test_auth_negative.py::test_temporary_code_authorization --alluredir allure-results


Командны для формирования отчетов:

result: allure serve allure-results

report: allure generate -c ./allure-results -o ./allure-report

