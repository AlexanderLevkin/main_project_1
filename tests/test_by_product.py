import time

import pytest
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


# @pytest.mark.run(order=2)
def test_by_product_1(set_group):
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    print('Start Test 1')
    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.select_product1()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = CheckoutPage(driver)
    cip.fill_in_checkout_field()

    pp = PaymentPage(driver)
    pp.payment()

    f = FinishPage(driver)
    f.get_screenshot()


# @pytest.mark.run(order=1)
def test_by_product_2(set_group):
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    print('Start Test 2')
    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.select_product2()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = CheckoutPage(driver)
    cip.fill_in_checkout_field()

    pp = PaymentPage(driver)
    pp.payment()

    f = FinishPage(driver)
    f.get_screenshot()


# @pytest.mark.run(order=3)
def test_by_product_3(set_group):
    driver = Chrome(service=Service(ChromeDriverManager().install()))
    print('Start Test 3')
    login = LoginPage(driver)
    login.autorization()

    mp = MainPage(driver)
    mp.select_product3()

    cp = CartPage(driver)
    cp.click_checkout_button()

    cip = CheckoutPage(driver)
    cip.fill_in_checkout_field()

    pp = PaymentPage(driver)
    pp.payment()

    f = FinishPage(driver)
    f.get_screenshot()
