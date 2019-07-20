from pages.WebGeneric import WebGeneric


class GooglePage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.un_xpath = "//input[@name='q']"
        self.wg = WebGeneric(self.driver)

    def fb_login(self, un, pwd):
        self.wg.enter("xpath", self.un_xpath, un)
        self.wg.enter("xpath", self.pwd_xpath, pwd)
        self.wg.submit("xpath", self.login_xpath)

    def fb_close(self):
        self.wg.submit("xpath", self.close_xpath)
