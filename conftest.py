import pytest
from selenium import webdriver


@pytest.fixture()
def browser():
    chrome_driver = webdriver.Chrome()
    chrome_driver.implicitly_wait(5)
    return chrome_driver

