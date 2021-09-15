import pytest
from selenium import webdriver

@pytest.fixture(scope='class')
def driv():
    driver = webdriver.Chrome()
    driver.get('https://www.baidu.com')
    # driver.implicitly_wait(3)
    yield driver
    # driver.close()


