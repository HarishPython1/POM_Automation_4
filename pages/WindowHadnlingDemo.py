import time

from selenium.webdriver import ActionChains
from pages.WebGeneric import WebGeneric
class WindowHandlingPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.login_xpath="//span[text()='Login']"
        self.email_tx_id="inputEmail"
        # self.dest_xpath="//*[@id='droppable']"
        self.wg=WebGeneric(self.driver)

    def window_handle(self):
        cur_win_id = self.driver.current_window_handle
        time.sleep(15)
        #self.locator("xpath",self.login_xpath)
        self.wg.submit("xpath",self.login_xpath)
        mul_win_id = self.driver.window_handles
        for id in mul_win_id:
            if (cur_win_id != id):
                self.driver.switch_to.window(id)
                time.sleep(3)
                self.wg.enter("id",self.email_tx_id,"Test")






        # var = self.locator("xpath",self.iframe_xpath)
        # self.driver.switch_to.frame(var)
        # s= self.locator("xpath",self.src_xpath)
        # d= self.locator("xpath",self.dest_xpath)
        # a1 = ActionChains(self.driver)
        # a1.drag_and_drop(s, d).perform()


