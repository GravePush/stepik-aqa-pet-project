from pages.main_page import MainPage


def test_guest_can_go_to_basket(browser, main_page):
    assert main_page.go_to_basket()


def test_guest_should_see_login_link(browser, main_page):
    assert main_page.should_be_login_link(), "Login link is not present."
