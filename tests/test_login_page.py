from pages.login_page import LoginPage

LOGIN_LINK_PAGE = "http://selenium1py.pythonanywhere.com/accounts/login/"


def test_guest_should_see_login_page(browser):
    page = LoginPage(browser, LOGIN_LINK_PAGE)
    page.open_page()
    page.should_be_login_page()
