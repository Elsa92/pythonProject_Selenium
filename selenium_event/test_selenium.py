import time

from selenium import webdriver
from selenium.webdriver.common.by import By


class TestHogwarts:

    def setup_class(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(5)

    def setup(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.ID,'kw').clear()

    def teardown_class(self):
        self.driver.close()

    def test_search(self):
        self.driver.find_element(By.ID,"kw").send_keys('自动化')
        self.driver.find_element(By.ID,"su").click()
        self.driver.find_element(By.LINK_TEXT,"自动化(一门科学技术) - 百度百科")

    def test_search1(self):
        self.driver.find_element(By.ID,"kw").send_keys('test')
        self.driver.find_element(By.ID,"su").click()



