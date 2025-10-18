from pages.main_page import MainPage

MAIN_PAGE_LINK = "http://selenium1py.pythonanywhere.com/"


def test_guest_can_click_on_basket(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open_page()
    page.click_on_basket()


def test_guest_should_see_login_link_on_main_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open_page()
    page.should_be_login_link()


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, MAIN_PAGE_LINK)
    page.open_page()
    page.go_to_login_page()
