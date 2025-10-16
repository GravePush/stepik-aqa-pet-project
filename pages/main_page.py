from selenium.webdriver.common.by import By

from .base_page import BasePage


class MainPage(BasePage):

    def go_to_basket(self):
        basket = self.is_element_clickable(By.CSS_SELECTOR, ".basket-mini a.btn.btn-default")
        basket.click()

    def should_be_login_link(self):
        self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid")
