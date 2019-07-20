import time

from selenium.webdriver.common.keys import Keys

from pages.WebGeneric import WebGeneric


class FBDashBoardPage(WebGeneric):
    def __init__(self, driver):
        WebGeneric.__init__(self, driver)
        self.search_xpath = "//input[@title='Search for products, brands and more']"
        self.wg = WebGeneric(self.driver)

    def fb_search(self, item_name):
        self.wg.enter("xpath", self.search_xpath, item_name)
        time.sleep(5)

    def fb_click_on_search(self):
        ele = self.wg.locator("xpath", self.search_xpath)
        ele.send_keys(Keys.ENTER)
        time.sleep(5)





    # def get_all_search_res(self):
    #     val = self.get_text_list("xpath", self.search_val_xpath)
    #     print("get_all_search_res" , val)
