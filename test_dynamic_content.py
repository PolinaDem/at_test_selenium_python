# content updated after refresh
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestDynamicContent:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver')
        self.driver.get('https://the-internet.herokuapp.com/dynamic_content')
        self.driver.implicitly_wait(5)

    def test_dynamic_image(self):
        z = self.driver.find_elements(By.TAG_NAME, "img")   # all images - list

        list = []                                           # create list with all image
        for img in z:
            b = img.get_attribute('outerHTML')              # "scr" of every image - str
            for i in b.split( ):                            # split data about image by space
                list.append(i)

        avatarlist = []                                     # create list with only checked "scr"
        for i in list:
            if 'Avatar' in i:
                avatarlist.append(i)
        a = avatarlist[0]                                   # personal data of every image
        b = avatarlist[1]
        c = avatarlist[2]

        self.driver.refresh()
        self.driver.implicitly_wait(5)

        z = self.driver.find_elements(By.TAG_NAME, "img")

        list = []
        for img in z:
            b = img.get_attribute('outerHTML')
            for i in b.split( ):
                list.append(i)

        avatarlist = []
        for i in list:
            if 'Avatar' in i:
                avatarlist.append(i)
        a1 = avatarlist[0]
        b1 = avatarlist[1]
        c1 = avatarlist[2]

        if (a != a1) and (b != b1) and (c != c1):
            print('All images updated')
        elif (a != a1) or (b != b1) or (c != c1):
            print('Some of images updated')
            if (a == a1):
                print('Error, images are the same in the first row')
            elif (b == b1):
                print('Error, images are the same in the second row')
            elif (c != c1):
                print('Error, images are the same in the third row')
        elif (a == a1) and (b == b1) and (c == c1):
            assert a != a1, 'Error, images are the same in the first row'
            assert b != b1, 'Error, images are the same in the second row'
            assert c != c1, 'Error, images are the same in the third row'

    def test_dynamic_text(self):
        a = self.driver.find_element(By.XPATH, "//div[@class='large-10 columns']").text
        b = self.driver.find_element(By.XPATH, "//div[@class='row']//div[@class='row']/following::"
                                                   "div[@class='large-10 columns']").text
        c = self.driver.find_element(By.XPATH, "//div[@class='row']//div[@class='row']/following::"
                                                   "div[@class='large-10 columns'][2]").text

        self.driver.refresh()
        self.driver.implicitly_wait(5)

        a1 = self.driver.find_element(By.XPATH, "//div[@class='large-10 columns']").text
        b1 = self.driver.find_element(By.XPATH, "//div[@class='row']//div[@class='row']/following::"
                                                   "div[@class='large-10 columns']").text
        c1 = self.driver.find_element(By.XPATH, "//div[@class='row']//div[@class='row']/following::"
                                                   "div[@class='large-10 columns'][2]").text

        if (a != a1) and (b != b1) and (c != c1):
            print('All texts updated')
        elif (a != a1) or (b != b1) or (c != c1):
            print('Some of texts updated')
            if (a == a1):
                print('Error, texts are the same in the first row')
            elif (b == b1):
                print('Error, texts are the same in the second row')
            elif (c != c1):
                print('Error, texts are the same in the third row')
        elif (a == a1) and (b == b1) and (c == c1):
            assert a != a1, 'Error, texts are the same in the first row'
            assert b != b1, 'Error, texts are the same in the second row'
            assert c != c1, 'Error, texts are the same in the third row'

    def teardown_method(self):
        self.driver.quit()


