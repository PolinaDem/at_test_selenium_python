# pop-up displays an ad on page load.
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class TestEntryAd:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/entry_ad')
        self.driver.implicitly_wait(5)

    def test_entry_ad(self):
        self.wait = WebDriverWait(self.driver, timeout=5)
        self.wait.until(lambda d: d.find_element(By.XPATH, "//div[@class='modal']").is_displayed())
        self.driver.find_element(By.XPATH, "//div[@style='display: block;']")
        self.driver.find_element(By.XPATH, "//div[@class='modal-footer']/p").click()
        self.driver.find_element(By.XPATH, "//div[@style='display: none;']")

    def teardown_method(self):
        self.driver.quit()