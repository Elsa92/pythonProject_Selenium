from time import sleep

from selenium import webdriver
from selenium.webdriver import TouchActions
from selenium.webdriver.common.by import By


class TestTouchActions:
    def setup(self):
        option = webdriver.ChromeOptions()
        option.add_experimental_option('w3c',False)
        self.driver = webdriver.Chrome(options=option)
        self.driver.implicitly_wait(3)
        self.driver.maximize_window()

    def teardown(self):
        self.driver.close()

    def test_touchactions(self):
        self.driver.get('https://www.baidu.com')
        ele=self.driver.find_element_by_id('kw')
        ele_search=self.driver.find_element_by_id('su')
        ele.send_keys('selenium测试')
        ele_search.click()
        # ele_next = self.driver.find_element(By.XPATH,'//*[@id="page"]/div/a[10]')
        actions = TouchActions(self.driver)
        actions.scroll_from_element(ele,0,10000)
        actions.perform()
        sleep(3)
        self.driver.find_element(By.XPATH, '//*[@id="page"]/div/a[10]').click()
        sleep(3)
