# check checkbox
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from colorama import Fore


class TestCheckBox:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/checkboxes')

    def test_open_page(self):
        try:
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'Checkboxes')]")
        except NoSuchElementException:
            print(Fore.RED + "\tWeb page is not open")
            self.driver.reviews.append(None)

    def test_original_position_of_checkboxes(self):
        first_checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        assert first_checkbox.is_selected() == False, "First checkbox is selected"
        second_checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
        assert second_checkbox.is_selected() == True, "Second checkbox is not selected"

    def test_changed_position_of_checkboxes(self):
        first_checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
        first_checkbox.click()
        assert first_checkbox.is_selected() == True, "First checkbox is not selected"
        second_checkbox = self.driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
        second_checkbox.click()
        assert second_checkbox.is_selected() == False, "Second checkbox is selected"

    def teardown_method(self):
        self.driver.quit()