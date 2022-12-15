# find broken images and return their count
from selenium import webdriver
import requests
from selenium.webdriver.common.by import By


class TestBrokenImages:

    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://the-internet.herokuapp.com/broken_images')

    def test_find_broken_img(self):
        broken_img = 0
        img_list = self.driver.find_elements(By.TAG_NAME, 'img')
        print('\nTotal number of images: ', str(len(img_list)), ' \n')

        for img in img_list:
            response = requests.get(img.get_attribute('src')).status_code
            if response != 200:
                print(img.get_attribute('outerHTML') + " is broken.")  
                broken_img = (broken_img + 1)

        print('Number of broken images: ', broken_img)

    def teardown_method(self):
        self.driver.quit()
