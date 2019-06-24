from data.testdata import *
from pages.WebGeneric import WebGeneric
class FB_LoginPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.un_id="email";
        self.pwd_id="pass";
        self.wg=WebGeneric(driver)

    def acti_login(self):
        self.wg.enter("id",self.un_id,USERNAME)
        self.wg.enter("id",self.pwd_id,PASSWORD)