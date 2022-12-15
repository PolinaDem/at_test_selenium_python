from selenium import webdriver
from selenium.webdriver.common.by import By


class TestClick:
    driver = ''

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver.exe')
        self.driver.implicitly_wait(2)
        self.driver.get('https://the-internet.herokuapp.com/add_remove_elements/')

    def test_click(self):
        add_btn = self.driver.find_element(By.XPATH, "//button[@onclick='addElement()']")
        add_btn.click()

        expected_delete_btn = 'Delete'
        actual_delete_btn = self.driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").text
        assert expected_delete_btn == actual_delete_btn, f'Expected button {expected_delete_btn}, but actual {actual_delete_btn}'
        self.driver.find_element(By.XPATH, "//button[@onclick='deleteElement()']").click()

    def teardown_method(self):
        self.driver.quit()
