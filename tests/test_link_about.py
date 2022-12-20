import time

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome

from pages.cart_page import CartPage
from pages.Client_information_page import CheckoutPage
from pages.finish_button import FinishPage
from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.payment_page import PaymentPage


def test_link_about():
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    print('Start Test')
    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.select_menu_about()

    f = FinishPage(driver)
    f.get_screenshot()






