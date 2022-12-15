# find the best locators in a table with no helpful locators, and a canvas element
import re
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from colorama import Fore


class TestChallengingDOM:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/challenging_dom')

    def test_open_page(self):
        try:
            self.driver.find_element(By.XPATH, "//*[text()='Challenging DOM']")  #Challenging DOM
        except NoSuchElementException:
            print(Fore.RED + "\tWeb page is not open")
            self.driver.reviews.append(None)

    def test_column_count(self):
        column_count = self.driver.find_elements(By.XPATH, "//div[@class='large-10 columns']//thead//tr/th")
        assert len(column_count) == 7, f"Expected column count: 7, but got: '{len(column_count)}'"

    def test_row_count(self):
        row_count = self.driver.find_elements(By.XPATH, "//div[@class='large-10 columns']//tbody//tr/td[1]")
        assert len(row_count) == 10, f"Expected row count: 10, but got: '{len(row_count)}'"

# edit button for first row (for example)
    def test_edit_btn(self):
        try:
            edit_btn = self.driver.find_element(By.XPATH, "//div[@class='large-10 columns']//tbody//tr[1]/td[7]//a[@href='#edit']")
            edit_btn.click()
            print(edit_btn.get_attribute('href'))
        except NoSuchElementException:
            print(Fore.RED + "\tEdit button not found")
            self.driver.reviews.append(None)

# delete button for second row (for example)
    def test_delete_btn(self):
        try:
            delete_btn = self.driver.find_element(By.XPATH, "//div[@class='large-10 columns']//tbody//tr[2]/td[7]//a[@href='#delete']")
            delete_btn.click()
            print(delete_btn.get_attribute('href'))
        except NoSuchElementException:
            print(Fore.RED + "\tDelete button not found")
            self.driver.reviews.append(None)

# btn_id is changed after click
    def test_blue_btn(self):
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=1]")
        btn_id = button.get_attribute("id")
        button.click()
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=1]")
        assert button.get_attribute("id") != btn_id

    def test_red_btn(self):
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=2]")
        btn_id = button.get_attribute("id")
        button.click()
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=2]")
        assert button.get_attribute("id") != btn_id

    def test_green_btn(self):
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=3]")
        btn_id = button.get_attribute("id")
        button.click()
        button = self.driver.find_element(By.XPATH, "//div[@class='large-2 columns']//a[position()=3]")
        assert button.get_attribute("id") != btn_id

    def test_answer_code(self):
        """
        Check the answer field rolls on page refresh
        """
        # grab the canvas generation script block, which contains the Answer buried in javascript
        img_script = self.driver.find_element(By.XPATH, "//div[@id='content']/script")
        # pick out the number after 'Answer' using regex
        old_answer = re.search(r"Answer:\s(\d+)", img_script).group(1)
        print(f"\nFound current Answer value: {old_answer}")
        # refresh page
        self.driver.refresh()
        # grab the canvas generation script block, which contains the Answer buried in javascript
        img_script = self.driver.find_element_by_xpath('//div[@id="content"]/script').get_attribute('innerHTML')
        # pick out the number after 'Answer' using regex
        new_answer = re.search(r"Answer:\s(\d+)", img_script).group(1)
        print(f"\nFound new Answer value: {new_answer}")

        assert old_answer != new_answer

    def teardown_method(self):
        self.driver.quit()


