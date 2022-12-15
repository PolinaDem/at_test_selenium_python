from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestDynamicControls():

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver')
        self.driver.get('https://the-internet.herokuapp.com/dynamic_controls')
        self.driver.implicitly_wait(5)

        self.wait = WebDriverWait(self.driver, timeout=3)

    def test_remove_checkbox(self):

        # click checkbox, click Remove btn
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Remove')]").click()

        # check message, check Add btn, checkbox is absent
        self.wait.until(lambda d: d.find_element(By.XPATH, "//button[contains(text(), 'Add')]"))
        self.driver.find_element(By.XPATH, "//p[contains(text(), 'gone!')]")
        try:
            assert self.driver.find_element(By.XPATH, "//input[@type='checkbox']")
        except NoSuchElementException:
            pass

        # click Add btn, check empty checkbox
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Add')]").click()
        self.driver.find_element(By.XPATH, "//p[contains(text(), 'back!')]")
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']")

    def test_disable_input(self):
        # check input locked, check Enable btn
        self.driver.find_element(By.XPATH, "//input[@type='text']")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Enable')]").click()
        self.wait.until(lambda d: d.find_element(By.XPATH, "//p[contains(text(), 'enabled!')]"))

        # put '111' in input
        self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys("test")
        self.driver.find_element(By.XPATH, "//button[contains(text(), 'Disable')]").click()
        self.wait.until(lambda d: d.find_element(By.XPATH, "//p[contains(text(), 'disabled!')]"))

    def teardown_method(self):
        self.driver.quit()
