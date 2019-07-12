from data.testdata import *
from pages.WebGeneric import WebGeneric
class LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        #self.driver=driver
        self.un_id="username";
        self.pwd_name="pwd";
        self.login_btn_xpath="//*[text()='Login ']"
        self.wg=WebGeneric(self.driver)

    def acti_login(self):
        # Logint to application - section 2 >>S2
        #self.driver.find_element_by_id("username").send_keys("admin")
        un= self.wg.get_val("Login","UserName")
        #self.wg.enter("id",self.un_id,USERNAME)
        self.wg.enter("id",self.un_id,un)
        #self.driver.find_element_by_name("pwd").send_keys("manager")

        self.wg.enter("name",self.pwd_name,self.wg.get_val("Login","Password"))
        #self.wg.enter("name",self.pwd_name,PASSWORD)
        #self.driver.find_element_by_xpath("//*[text()='Login ']").click()
        self.wg.submit("xpath",self.login_btn_xpath)
        self.wg.get_screenshot()