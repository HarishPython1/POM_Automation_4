import pytest
from data.testdata import *

import os
@pytest.fixture(scope='function')#conftest will be executed for each and every test
#@pytest.fixture(scope='class')#conftest will be executed only one time
#@pytest.fixture(scope='session')#conftest will be executed only one time
def test_setup(request):
    from selenium import webdriver
    dir = os.getcwd()+"\\drivers"
    driver = webdriver.Chrome(
        executable_path=dir+"\\chromedriver.exe")
    driver.get(URL)
    driver.implicitly_wait(MED_WAIT)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()
