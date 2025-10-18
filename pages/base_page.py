from selenium.common.exceptions import TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser: WebDriver, url: str):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    def go_to_page(self, how: str, what: str):
        try:
            page = self.is_element_present(how, what)
            page.click()
        except TimeoutException:
            return False
        return True

    def is_element_present(self, how: str, what: str):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.presence_of_element_located((how, what))
            )
            return element
        except TimeoutException:
            return False

    def is_element_clickable(self, how: str, what: str):
        try:
            element = WebDriverWait(self.browser, 5).until(
                EC.element_to_be_clickable((how, what))
            )
            return element
        except TimeoutException:
            return False

