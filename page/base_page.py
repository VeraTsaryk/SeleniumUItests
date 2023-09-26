from selenium.webdriver.common.by import By


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def find(self, args):
        return self.browser.find_element(*args)

    # login_selector = (By.ID, 'email')
    # password_selector = (By.ID, 'pass')
    # button_selector = (By.ID, 'send2')
    # error_selector = (By.CSS_SELECTOR, '[data-ui-id="message-error"]')