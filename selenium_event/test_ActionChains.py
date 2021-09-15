from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class TestActionChains:
    def setup(self):
        self.driver = webdriver.Chrome()
        # self.driver.implicitly_wait(5)

    # def setup_class(self):
    #     self.driver = webdriver.Chrome()
    #     self.driver.get('https://www.baidu.com')
    #     self.driver.maximize_window()
    #     self.driver.implicitly_wait(10)
    #
    # def setup(self):
    #     self.driver.get('https://www.baidu.com')
    #     self.driver.implicitly_wait(10 )
    #
    # def teardown(self):
    #     self.driver.close()

    @pytest.mark.skip
    def test_click(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element(By.XPATH,'//*[@id="kw"]').send_keys('自动化测试')
        element_click = self.driver.find_element(By.XPATH,'//*[@id="su"]')
        actions = ActionChains(self.driver)
        actions.click(element_click)
        actions.perform()


    @pytest.mark.skip
    def test_movetoelement(self):
        self.driver.get('https://www.baidu.com')
        element_movetoelement= self.driver.find_element(By.XPATH, '//*[@id="u1"]/span')
        actions = ActionChains(self.driver)
        actions.move_to_element(element_movetoelement)
        actions.perform()

    @pytest.mark.skip
    def test_dragdrop(self):
        self.driver.get("http://sahitest.com/demo/dragDropMooTools.htm")
        drag_element= self.driver.find_element_by_id("dragger")
        drop_element= self.driver.find_element_by_xpath("/html/body/div[2]")
        actions = ActionChains(self.driver)
        # actions.drag_and_drop(drag_element,drop_element).perform()
        # actions.click_and_hold(drag_element).release(drop_element).perform()
        actions.click_and_hold(drag_element).move_to_element(drop_element).release().perform()

    def test_keys(self):
        self.driver.get('https://sahitest.com/demo/label.htm')
        ele_key1 = self.driver.find_element_by_xpath('/html/body/label[1]/input')
        ele_key2 = self.driver.find_element_by_xpath('/html/body/label[2]/table/tbody/tr/td[2]/input')
        actions = ActionChains(self.driver)
        actions.click(ele_key1)
        actions.send_keys('username').pause(1)
        sleep(3)
        actions.send_keys(Keys.SPACE).pause(1)
        sleep(3)
        actions.send_keys('Toms').pause(1)
        sleep(3)
        actions.send_keys(Keys.BACK_SPACE).pause(1)
        sleep(3)
        actions.key_down(Keys.CONTROL).send_keys('a').send_keys('c').key_up(Keys.CONTROL).pause(1)
        sleep(3)
        actions.click(ele_key2)
        actions.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).pause(1)
        sleep(3)
        actions.perform()




