import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestWait:

    def setup(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.baidu.com')
        # 隐式等待
        self.driver.implicitly_wait(3)


    def test_wait(self):
        # driv.find_element(By.ID,'kw').send_keys('自动化测试')
        # driv.find_element(By.XPATH,'//*[@id="kw"]').send_keys('自动化测试')
        self.driver.find_element(By.CSS_SELECTOR, '#kw').send_keys('自动化测试')
        # 直接等待
        # time.sleep(3)
        self.driver.find_element(By.ID,'su').click()
        # time.sleep(3)
        # 显示等待
        # def wait(x):
        #     return len(self.driver.find_elements(By.XPATH,'//*[@id="1"]/div[1]/div[1]/p[2]/a[1]')) >=1
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, '//*[@id="1"]/div[1]/div[1]/p[2]/a[1]')))
        self.driver.find_element(By.XPATH,'//*[@id = "1"]//h3//a[1]').click()




