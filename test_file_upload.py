from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui


class TestFileUpload:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver')
        self.driver.get("https://the-internet.herokuapp.com/upload")
        self.driver.implicitly_wait(5)

    def test_upload_by_btn(self):
        drop = self.driver.find_element(By.XPATH, "//input[@id='file-upload']")
        drop.send_keys("D://WORK/PycharmProjects/at_test_selenium_python/test_files_AT/6543A349.png")
        self.driver.find_element(By.XPATH, "//input[@class='button']").click()
        self.driver.find_element(By.XPATH, "//h3[contains(text(),'Uploaded!')]")

    def test_upload_by_window(self):
        self.driver.find_element(By.XPATH, "//div[@id='drag-drop-upload']").click()
        pyautogui.write(r'\\D:\WORK\PycharmProjects\at_test_selenium_python\test_files_AT\6543A349.png', interval=0.1)
        pyautogui.press('ENTER')


    def teardown_method(self):
        self.driver.quit()
