from page.simple_button_page import SimpleButtonPage
from conftest import browser # Vera, look at this line


def test_button_exist(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    assert simple_page.button().is_displayed()


def test_button_clicked(browser):
    simple_page = SimpleButtonPage(browser)
    simple_page.open()
    simple_page.button().click()
    assert 'Submitted' == simple_page.result().text