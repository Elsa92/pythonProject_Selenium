from time import sleep

from selenium_frame_window.Base import Base


class TestFileAlert(Base):

    def test_file_upload(self):
        self.driver.get('https://image.baidu.com/')
        self.driver.find_element_by_xpath('//*[@id="sttb"]/img[1]').click()
        self.driver.find_element_by_id('stfile').send_keys('C:/Users/Elsa/Pictures/123.PNG')
        sleep(3)