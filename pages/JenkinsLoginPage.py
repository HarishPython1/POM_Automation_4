from data.testdata import *
from pages.WebGeneric import WebGeneric


class JenkinsLoginPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        # self.driver=driver
        self.un_id = "j_username";
        self.pwd_name = "j_password";
        self.login_btn_xpath = "Submit"
        self.wg = WebGeneric(self.driver)

    def jenkins_login(self):
        un = self.wg.get_val("Login", "UserName")
        self.wg.enter("id", self.un_id, un)
        self.wg.enter("name", self.pwd_name, self.wg.get_val("Login", "Password"))
        self.wg.submit("xpath", self.login_btn_xpath)
        self.wg.get_screenshot()
