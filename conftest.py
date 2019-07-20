import pytest
from data.testdata import *


@pytest.fixture(scope='function')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:\\Users\\Hareesh\\PycharmProjects\\POM_Automation_5\\drivers\\chromedriver.exe")
    driver.get(URL)
    driver.implicitly_wait(MED_WAIT)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
