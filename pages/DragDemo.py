from selenium.webdriver import ActionChains
from pages.WebGeneric import WebGeneric
class DragPage(WebGeneric):
    def __init__(self,driver):
        WebGeneric.__init__(self,driver)
        self.iframe_xpath="//iframe[@class='demo-frame']"
        self.src_xpath="//*[@id='draggable']"
        self.dest_xpath="//*[@id='droppable']"
        self.wg=WebGeneric(self.driver)

    def jquery_drag(self):
        var = self.locator("xpath",self.iframe_xpath)
        self.driver.switch_to.frame(var)
        s= self.locator("xpath",self.src_xpath)
        d= self.locator("xpath",self.dest_xpath)
        a1 = ActionChains(self.driver)
        a1.drag_and_drop(s, d).perform()


