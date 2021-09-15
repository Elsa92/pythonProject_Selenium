from time import sleep

from selenium import webdriver

from selenium_frame_window.Base import Base


class TestWindow(Base):

    def test_window(self):
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="u1"]/a').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        self.driver.find_element_by_xpath('//*[@class="pass-reglink pass-link"]').click()
        # print(self.driver.current_window_handle)
        # print(self.driver.window_handles)
        windows = self.driver.window_handles

        self.driver.switch_to.window(windows[-1])
        self.driver.find_element_by_id('TANGRAM__PSP_4__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_4__phone').send_keys('15092078614')
        sleep(3)
        self.driver.switch_to.window(windows[0])
        self.driver.find_element_by_id('TANGRAM__PSP_11__footerULoginBtn').click()
        self.driver.find_element_by_id('TANGRAM__PSP_11__userName').send_keys('username')
        self.driver.find_element_by_id('TANGRAM__PSP_11__password').send_keys('password')
        self.driver.find_element_by_id('TANGRAM__PSP_11__submit').click()
        sleep(3)


