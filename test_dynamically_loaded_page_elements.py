# add explicit and implicit expectation of elements
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestDynamicElements:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver')
        self.driver.get('https://the-internet.herokuapp.com/dynamic_loading')
        self.driver.implicitly_wait(5)

    # неявное ожидание Implicit expectation
    def test_element_is_hidden(self):
        self.driver.get('https://the-internet.herokuapp.com/dynamic_loading/1')
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()
        self.driver.implicitly_wait(5)
        msg = self.driver.find_element(By.XPATH, "//div[@id='finish']/h4").text
        print(msg)

    # явное ожидание Explicit wait
    def test_element_after_the_fact(self):
        self.wait = WebDriverWait(self.driver, timeout=5)
        self.driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Start')]").click()
        msg = self.wait.until(lambda d: d.find_element(By.XPATH, "//div[@id='finish']/h4").text)
        print(msg)

    def teardown_method(self):
        self.driver.quit()