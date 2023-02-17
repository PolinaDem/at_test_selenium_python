import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestFileUpload:
    home = "//a[@href='#home']"
    news = "//a[@href='#news']"
    contact = "//a[@href='#contact']"
    about = "//a[@href='#about']"
    search_words = (home, news, contact, about)

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://the-internet.herokuapp.com/floating_menu")
        self.driver.implicitly_wait(5)

    @pytest.mark.parametrize('search_query', search_words)
    def test_floating_menu(self, search_query):
        self.driver.execute_script("window.scrollTo(0, 1080)")
        self.driver.find_element(By.XPATH, "//div[@id='menu']")
        self.driver.find_element(By.XPATH, search_query)


    def teardown_method(self):
        self.driver.quit()
