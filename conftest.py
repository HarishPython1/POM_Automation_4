import pytest

@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_4/drivers/chromedriver.exe")
    driver.get("http://localhost/login.do")
    driver.implicitly_wait(30)
    request.cls.driver = driver