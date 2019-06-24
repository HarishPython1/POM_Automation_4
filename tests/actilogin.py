from selenium import webdriver
from pages.LoginPage import LoginPage
from pages.HomePage import HomePage
import pytest

@pytest.mark.usefixtures("test_setup")
class  TestLogin:
    def test_login(self):
        driver=self.driver
        lp=LoginPage(driver)
        lp.acti_login()

    # def test_logout(self):
    #     driver = self.driver
    #     hp=HomePage(driver)
    #     hp.acti_logout()


# def test_logout():
#     driver.find_element_by_id("logoutLink").click()