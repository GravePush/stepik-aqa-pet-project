from .base_page import BasePage
from .locators import MainPageLocators
from .login_page import LoginPage


class MainPage(BasePage):
    def click_on_basket(self):
        assert self.is_element_clickable(*MainPageLocators.BASKET_BUTTON), "Button is not clickable."

    def go_to_login_page(self):
        assert self.go_to_page(*MainPageLocators.LOGIN_LINK)
        login_page = LoginPage(self.browser, self.browser.current_url)
        login_page.should_be_login_page()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not present."
