from urllib.parse import urlparse
from base.locators import AuthLocators
import time
import allure

class BasePage(object):
    # конструктор класса - специальный метод с ключевым словом __init__
    # Нам нужны объект веб-драйвера, адрес страницы и время ожидания элементов
    def __init__(self, driver, url="https://b2c.passport.rt.ru/auth"):
        self.driver = driver
        self.url = url

    def get_relative_link(self):
        url = urlparse(self.driver.current_url)
        return url.path

    def open_page(self, url):
        self.driver.get(url)

    def back(self):
        pass


