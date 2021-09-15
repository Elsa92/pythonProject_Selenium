from time import sleep

from selenium.webdriver import ActionChains

from selenium_frame_window.Base import Base


class TestFrame(Base):
    def test_frame(self):
        self.driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
        self.driver.switch_to.frame('iframeResult')
        print(self.driver.find_element_by_id('draggable').text)
        ele_drag = self.driver.find_element_by_id('draggable')
        ele_drop = self.driver.find_element_by_id('droppable')
        print(self.driver.find_element_by_id('droppable').text)
        actions = ActionChains(self.driver)
        actions.click_and_hold(ele_drag).release(ele_drop).pause(1)
        sleep(3)
        self.driver.switch_to.parent_frame()
        self.driver.switch_to_default_content()
        print(self.driver.find_element_by_id('submitBTN').text)