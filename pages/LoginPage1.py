from pages.WebGeneric import WebGeneric
from data.testdata import *

class LoginPage1(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.un_id = "username"
        self.pss_name="pwd"
        self.wg=WebGeneric(self.driver)

    def enter_un(self):
        self.wg.enter("id",self.un_id,USERNAME)


    def enter_pwd(self):
        self.wg.enter("name",self.pss_name,PASSWORD)