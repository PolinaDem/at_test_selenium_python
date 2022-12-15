# при наведении на панель сверху появляется модал. окно (курсор должен быть в рабочей области в начале теста)
# If cursor was not directly in workspace after the start of test, then test failed
from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import pyautogui


class TestExitIntent:

    def setup_method(self):
        self.driver = webdriver.Chrome(executable_path='D:\WORK\PycharmProjects\what_can_I_do\chromedriver')
        self.driver.get('https://the-internet.herokuapp.com/exit_intent')
        self.driver.implicitly_wait(5)

    def test_exit_intent(self):
        # try to return cursor to page
        action = ActionChains(self.driver)
        action.move_by_offset(550, 550)
        action.perform()
        # move cursor to toolbar
        pyautogui.moveTo(100, 100)
        # check modal window
        self.driver.find_element(By.XPATH, "//div[@class='modal']").is_displayed()
        modalWindowTitle = self.driver.find_element(By.XPATH, "//div[@id='ouibounce-modal']//h3")
        modalWindowText = modalWindowTitle.get_attribute("innerText")
        assert modalWindowText == "THIS IS A MODAL WINDOW", "Modal window not open"

        self.driver.find_element(By.XPATH, "//div[@class='modal-footer']/p").click()

    def teardown_method(self):
        self.driver.quit()