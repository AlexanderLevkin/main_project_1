from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import time

from base.base_class import Base


class LoginPage(Base):

    url = 'https://www.saucedemo.com'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    def autorization(self, user_name, login_password):
        # Authorization on site
        username_field = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//input[@id="user-name"]')))
        username_field.send_keys(user_name)
        password_field = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//input[@id="password"]')))
        password_field.send_keys(login_password)
        time.sleep(1)
        login_button = WebDriverWait(self.driver, 30).until(
            expected_conditions.element_to_be_clickable((By.XPATH, '//input[@id="login-button"]')))
        login_button.click()
        time.sleep(1)
        print("Login into site\n")