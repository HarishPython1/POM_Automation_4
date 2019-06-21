from selenium import webdriver
from data.testdata import *
from pages.WebGeneric import WebGeneric
class LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.driver=driver
        self.un_id="username";
        self.pwd_name="pwd";
        self.login_btn_xpath="//*[text()='Login ']"

    def acti_login(self):
        # Logint to application - section 2 >>S2
        wg=WebGeneric(self.driver)
        #self.driver.find_element_by_id("username").send_keys("admin")
        wg.enter(self.un_id,USERNAME)
        #self.driver.find_element_by_name("pwd").send_keys("manager")
        wg.enter(self.pwd_name,PASSWORD)
        #self.driver.find_element_by_xpath("//*[text()='Login ']").click()
        wg.submit(self.login_btn_xpath)