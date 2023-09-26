from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from page.simple_button_page import SimpleButtonPage

logins = ["user1@mail.com", "user2@mail.com", "user3@mail.com"]
passwords = ["12jdj", "65dfs", "dfdfs858585"]


def generate_pairs():
    pairs = []
    for login in logins:
        for passw in passwords:
            pairs.append(pytest.param((login, passw), id=f'{login},{passw}'))
    return pairs


# @pytest.mark.parametrize(
#     'creds',
#     [
#        pytest.param(("user1@mail.com" ,"12jdj") , id='user1@mail.com" ,"12jdj'),
#        pytest.param(("user2@mail.com","65dfs"), id= 'user2@mail.com","65dfs'),
#        pytest.param(("user3@mail.com","dfdfs858585"), id='user3@mail.com","dfdfs858585')
#     ]
#     )
@pytest.mark.parametrize('creds', generate_pairs())
def test_login(creds):
    login, password = creds
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get('https://magento.softwaretestingboard.com/customer/account/login')
    driver.find_element(By.ID, 'email').send_keys(login)
    driver.find_element(By.ID, 'pass').send_keys(password)
    driver.find_element(By.ID, 'send2').click()
    error_text = driver.find_element(By.CSS_SELECTOR, '[data-ui-id="message-error"]').text
    assert ('The account sign-in was incorrect or your account is disabled temporarily. Please wait and try again later.' == error_text)
