# this example demonstrates when elements on a page change by disappearing/reappearing on each page load
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class TestDisappearingElements:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/disappearing_elements')

    def test_disappearing_elements(self):
        try:
            if self.driver.find_element(By.XPATH, "//a[contains(text(), 'Gallery')]"):
                print("Element 'Gallery' was found")
                #  check new page
                self.driver.find_element(By.XPATH, "//a[@href='/gallery/']").click()
                self.driver.implicitly_wait(3)
                if self.driver.find_element(By.XPATH, "//h1[contains(text(), 'Not Found')]"):
                    print("New page opened")
        except NoSuchElementException:
            print("Element 'Gallery' not found")
            self.driver.refresh()

    def teardown_method(self):
        self.driver.quit()