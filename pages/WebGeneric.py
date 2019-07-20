from pages.LocatorGeneric import LocatorGeneric

class WebGeneric(LocatorGeneric):
    def __init__(self, driver):
        LocatorGeneric.__init__(self, driver)
        self.lc = LocatorGeneric(self.driver)

    #enter text values[locator_type, locator_val, input_val]
    def enter(self, locator_type, locator_val, input_val):
        var = self.locator(locator_type, locator_val)
        var.send_keys(input_val)
        self.get_screenshot("Entered "+input_val+" in text field")

    def submit(self, locator_type, locator_val):
        var = self.locator(locator_type, locator_val)
        var.click()
        self.get_screenshot("Clicked on a web element ")

    def get_text_list(self, loc_type, locator_val):
        elements = self.mul_locator(loc_type, locator_val)
        l = []
        for i in elements:
            val = i.text
            l.append(val)
            print(l)
        return l
