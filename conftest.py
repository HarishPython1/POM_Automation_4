import pytest
from data.testdata import *

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_4/drivers/chromedriver.exe")
    driver.get(URL)
    driver.implicitly_wait(MED_WAIT)
    request.cls.driver = driver