from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TestBasicAuthentication:
    chrome_options = Options()
    #chrome_options.add_argument("--no-sandbox")    # отключение ограничений безопасности
    #chrome_options.add_argument('disable-notifications')
    #chrome_options.add_argument("window-size=1280,720")

    def setup_method(self):
        webdriver_service = Service("D:\WORK\PycharmProjects\what_can_I_do\chromedriver.exe")
        self.driver = webdriver.Chrome(service=webdriver_service, options=self.chrome_options)

    def test_basic_authentication(self):
        user = 'admin'
        passw = 'admin'
        self.driver.get(f"https://{user}:{passw}@the-internet.herokuapp.com/basic_auth")

        test_element = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//p[contains(text(), 'Congratulations!')]")))

        print(test_element.text)

    def teardown_method(self):
        self.driver.quit()
