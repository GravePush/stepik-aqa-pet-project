import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.main_page import MainPage


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language!")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})

    browser = webdriver.Chrome(options=options)
    print("\nstart chrome browser for test..")

    yield browser, language

    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function")
def main_page(browser):
    browser, language = browser
    link = "http://selenium1py.pythonanywhere.com/"
    browser.get(link)
    page = MainPage(browser, link)
    page.open_page()
    yield page
