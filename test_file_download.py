from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestFileDownload:

    def setup_method(self):

        options = webdriver.ChromeOptions()
        prefs = {'download.default_directory': 'D:\\WORK\\PycharmProjects\\what_can_I_do\\test_files_AT\\'}
        options.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver', options=options)

        self.driver.get("https://the-internet.herokuapp.com/download")
        self.driver.implicitly_wait(5)

    def test_download(self):
        self.driver.find_element(By.XPATH, "//div[@class='example']/a[@href][1]").click()
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
