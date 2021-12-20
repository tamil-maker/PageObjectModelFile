import pytest
from selenium import webdriver
from Config.config import TestData

@pytest.fixure(params=["chrome","firefox"],scope='class')
def init_driver(request):
    if request.param == 'chrome':
        web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLR_PATH)
    if request.param == 'firefox':
        web_driver = webdriver.Firefox(executable_path=TestData.FIREFOX_EXECUTABLR_PATH)
        request.cls.driver = web_driver
        yield
        web_driver.close()