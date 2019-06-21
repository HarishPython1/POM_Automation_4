from pages.LocatorGeneric import LocatorGeneric
class WebGeneric(LocatorGeneric):
    def __init__(self,driver):
        LocatorGeneric.__init__(self,driver)
        self.driver=driver

    def enter(self,locator,input_val):
        #self.driver.find_element_by_id(locator).send_keys(input_val)
        self.locator("locatortype","locator_val").send_keys(input_val)

    def submit(self,locator):
        #self.driver.find_element_by_id(locator).click()
        self.locator("locatortype", "locator_val").click()