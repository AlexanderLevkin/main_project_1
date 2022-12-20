from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time

from base.base_class import Base


class CheckoutPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    first_name_field = "//*[@id='first-name']"
    last_name_field = "//*[@id='last-name']"
    zip_postal_code_field = "//*[@id='postal-code']"
    continue_button = "//*[@id='continue']"

    # Getters
    def get_first_name_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.first_name_field)))

    def get_last_name_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.last_name_field)))

    def get_zip_postal_code_field(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.zip_postal_code_field)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions
    def input_first_name(self, first_name):
        self.get_first_name_field().send_keys(first_name)
        print(f"FILL IN THE FIRST NAME FIELD...{first_name}")

    def input_last_name(self, last_name):
        self.get_last_name_field().send_keys(last_name)
        print(f"FILL IN THE LAST NAME FIELD...{last_name}")

    def input_zip_postal_code(self, zip_postal_code):
        self.get_zip_postal_code_field().send_keys(zip_postal_code)
        print(f"FILL IN THE ZIP OR POSTAL CODE...{zip_postal_code}")

    def click_continue_button(self):
        self.get_continue_button().click()

    # Methods
    def fill_in_checkout_field(self):
        self.get_current_url()
        time.sleep(2)
        self.input_first_name("ALEXANDER")
        time.sleep(1)
        self.input_last_name("LEVKIN")
        time.sleep(1)
        self.input_zip_postal_code("211500")
        time.sleep(1)
        self.click_continue_button()
