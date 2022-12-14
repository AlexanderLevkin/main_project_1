import datetime
import time


class Base:
    def __init__(self, driver):
        self.driver = driver

    """Method Get current url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current url {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("GOOD VALUE WORLD")


    """Method assert url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("GOOD VALUE URL")

    """Method screen shot"""

    def get_screenshot(self):
        now_date = datetime.datetime.utcnow().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot ' + now_date + '.png'
        self.driver.save_screenshot('/Users/alexanderlevkin/Desktop/LESSONS/main_project/screen/' + name_screenshot)
