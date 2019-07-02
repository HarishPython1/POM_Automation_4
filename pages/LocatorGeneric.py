from selenium.common.exceptions import *
class LocatorGeneric:
    def __init__(self, driver):
        self.driver = driver
    def locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_element_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_element_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_element_by_xpath(locator_val)
            elif loc_type == "tagname":
                ele = self.driver.find_element_by_tag_name(locator_val)
            return ele
        except NoSuchElementException as e:
            print(e)
        except ElementNotInteractableException as e:
            print(e)
        except WebDriverException as e:
            print(e)
        except NoSuchWindowException as e:
            print(e)
        except UnexpectedTagNameException as e:
            print(e)
        except ElementClickInterceptedException as e:
            print(e)
        except SessionNotCreatedException as e:
            print(e)
        except StaleElementReferenceException as e:
            print(e)
        except Exception as e:
            print(e)









