from selenium.webdriver.common.by import By

class AuthLocators:

    AUTH_MAIN = (By.CSS_SELECTOR, "#app-container")
    AUTH_LEFT_BLOCK = (By.CSS_SELECTOR, "#page-left")
    AUTH_RIGHT_BLOCK = (By.CSS_SELECTOR, "#page-right")
    AUTH_MENU = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.tabs-input-container > div.rt-tabs.rt-tabs--orange.rt-tabs--small.tabs-input-container__tabs")
    AUTH_TAB_PHONE = (By.CSS_SELECTOR, "#t-btn-tab-phone")
    AUTH_TAB_MAIL = (By.CSS_SELECTOR, "#t-btn-tab-mail")
    AUTH_TAB_LOGIN = (By.CSS_SELECTOR, "#t-btn-tab-login")
    AUTH_TAB_LS = (By.CSS_SELECTOR, "#t-btn-tab-ls")
    AUTH_SLOGAN = (By.CSS_SELECTOR, "#page-left > div > div.what-is")
    AUTH_INCORREKT_LOGIN_OR_PASSWORD = (By.CSS_SELECTOR, "#form-error-message")
    AUTH_CAPTCHA_IMG = (By.XPATH, "//*[@id='page-right']/div/div[1]/div[2]/form/div[3]/div[1]/div[1]/img")
    AUTH_CAPTCHA_INPUT = (By.CSS_SELECTOR,"#captcha")
    AUTH_REFRESH_CAPTCHA = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div.card-container__content > form > div.rt-captcha.login-form__captcha > div.rt-captcha__left > div.rt-captcha__reload-con > svg")
    AUTH_EXIT = (By.XPATH, '//*[@id="logout-btn"]')
    AUTH_TAB_FORGOTT_PASS = (By.CSS_SELECTOR, "#forgot_password")
    AUTH_TAB_TEMP_CODE = (By.CSS_SELECTOR, "#back_to_otp_btn")
    AUTH_TEMP_CODE_TEXT =(By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > h1")

    AUTH_CAPTCHA_IMG_FORG = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.rt-captcha.reset-form__captcha > div.rt-captcha__left > div.rt-captcha__image-con > img")
    AUTH_CAPTCGA_INPUT_FORG = (By.CSS_SELECTOR, "#captcha")
    AUTH_BTN_FORG_PASS_NEXT = (By.CSS_SELECTOR, "#reset")
    Auth_FORGOTPASS_TEXT = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > h1")



    AUTH_USER_NAME = (By.CSS_SELECTOR, "#app > main > div > div.home > div.base-card.home__info-card > div.user-info.home__user-info > div.user-info__name-container > h2")

    AUTH_EMAIL_PHONE_NUMBER = (By.CSS_SELECTOR, '#username')
    AUTH_PASS = (By.CSS_SELECTOR, '#password')
    AUTH_BTN = (By.CSS_SELECTOR, '#kc-login')
    AUTH_PASS_MASK = (By.CSS_SELECTOR, '.rt-eye-icon')
    AUTH_FORGOT_PASS_LINK = (By.CSS_SELECTOR, '#forgot_password')
    AUTH_USER_AGREEMENT_LINK = (By.CSS_SELECTOR, '#rt-auth-agreement-link')
    AUTH_ERROR_LGN = (By.CSS_SELECTOR, '#form-error-message')
    AUTH_PHONE_NUMBER=(By.CSS_SELECTOR,'#username')

    AUTH_HELP_LINK = (By.CSS_SELECTOR, '#faq-open')
    AUTH_REGISTRATION = (By.CSS_SELECTOR, '#kc-register')

    AUTH_CITY = (By.XPATH,'//*[@id="page-right"]/div/div[1]/div/form/div[2]/div/div/input')
    AUTH_FIRST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[1]/div/input')
    AUTH_LAST_NAME = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/div[1]/div[2]/div/input')
    AUTH_EMAIL_OR_PHONE = (By.XPATH, '//*[@id="address"]')
    AUTH_REGISTRATION_BTN = (By.XPATH, '//*[@id="page-right"]/div/div[1]/div/form/button')
    AUTH_REGISTRATION_PASS = (By.XPATH, '//*[@id="password"]')
    AUTH_PASS_CONFIRM = (By.XPATH, '//*[@id="password-confirm"]')
    AUTH_REGISTRATION_CONFIRM_EMAIL = (By.CSS_SELECTOR, "#page-right > div > div > h1")
    AUTH_REGISTRATION_ERR = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.base-modal-wrapper.card-modal > div > div > h2")
    AUTH_REGISTRATION_PASS_ATTENTHION_Lit = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__password > span")
    AUTH_REGISTRATION_INPUT_NAME_ATTENTION = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.name-container > div:nth-child(1) > span")
    AUTH_REG_PASS_LENGTH = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__password > span")
    AUTH_REG_PASS_NOT_SAME = (By.CSS_SELECTOR, "#page-right > div > div.card-container__wrapper > div > form > div.new-password-container > div.rt-input-container.rt-input-container--error.new-password-container__confirmed-password > span")