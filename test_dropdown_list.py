# check dropdown
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDropdown:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/dropdown')

    def test_first_option(self):
        self.driver.find_element(By.ID, "dropdown").click()
        self.driver.find_element(By.XPATH, "//option[@value='1']").click()
        self.driver.find_element(By.XPATH, "//option[@value='1'][@selected='selected']")

    def test_second_option(self):
        self.driver.find_element(By.ID, "dropdown").click()
        self.driver.find_element(By.XPATH, "//option[@value='2']").click()
        self.driver.find_element(By.XPATH, "//option[@value='2'][@selected='selected']")

    def teardown_method(self):
        self.driver.quit()