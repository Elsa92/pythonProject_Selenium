from time import sleep

from selenium_js.Base import Base


class TestJs(Base):

    def test_js_scroll(self):
        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').send_keys('selenium测试')
        # self.driver.find_element_by_id('su').click()
        ele = self.driver.execute_script("return document.getElementById('su')")
        ele.click()
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        sleep(3)
        self.driver.find_element_by_xpath("//*[@id='page']/div/a[last()]").click()
        sleep(3)
        for code in [
            'document.tile', 'return JSON.stringify(performance.timing)'
        ]:
            print(self.driver.execute_script(code))
        # print(self.driver.execute_script('return document.tile; return JSON.stringify(performance.timing)'))


    def test_date(self):
        self.driver.get('https://www.12306.cn/index/')
        date_js= "document.getElementById('train_date').removeAttribute('readonly')"
        self.driver.execute_script(date_js)
        sleep(2)
        date_js_1="document.getElementById('train_date').value='2021-10-01'"
        self.driver.execute_script(date_js_1)
        a = self.driver.find_element_by_id('train_date').text
        print(f'当前所选的日期为:{a}')

        # self.driver.execute_script("a = document.getElementById('train_date');a.removeAttribute('readonly')")
        # self.driver.execute_script("document.getElementById('train_date').value='2021-10-01'")
        sleep(3)
        # print(self.driver.execute_script("return document.getElementById('train_date').value"))