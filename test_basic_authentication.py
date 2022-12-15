from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasicAuthentication:

    def setup_method(self):
        self.driver = webdriver.Chrome()

    def test_basic_authentication(self):
        user = 'admin'
        passw = 'admin'
        self.driver.get(f"https://{user}:{passw}@the-internet.herokuapp.com/basic_auth")

        test_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Congratulations!')]")))

        print(test_element.text)

    def teardown_method(self):
        self.driver.quit()
