# login into the secure area
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestLoginPage:
    wrong_usernames = ('', ' ', 'tomsmith ', 'Tomsmith')
    wrong_passwords = ('', ' ', 'SuperSecretPassword! ', 'superSecretPassword!')

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/login')
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('tests_query', wrong_usernames)
    def test_username(self, tests_query):
        field_username = self.driver.find_element(By.ID, 'username')
        field_username.send_keys(tests_query, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Your username is invalid!')]")

    @pytest.mark.parametrize('tests_query', wrong_passwords)
    def test_password(self, tests_query):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        field_password = self.driver.find_element(By.ID, 'password')
        field_password.send_keys(tests_query, Keys.ENTER)
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'Your password is invalid!')]")

    def test_login(self):
        self.driver.find_element(By.ID, 'username').send_keys('tomsmith')
        self.driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
        self.driver.find_element(By.XPATH, "//button[@class='radius']").click()
        self.driver.find_element(By.XPATH, "//div[contains(text(), 'You logged into a secure area!')]")

    def teardown_method(self):
        self.driver.quit()
