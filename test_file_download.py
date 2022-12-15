from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestFileDownload:

    def setup_method(self):

        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': 'D:\\WORK\\PycharmProjects\\at_test_selenium_python\\test_files_AT\\'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(options=options)

        self.driver.get("https://the-internet.herokuapp.com/download")
        self.driver.implicitly_wait(5)

    def test_download(self):
        self.driver.find_element(By.XPATH, "//div[@class='example']/a[@href][1]").click()
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
