import allure
from selenium.common.exceptions import *
import xlrd
import os
import moment
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

    def get_val(Sheet_Name, input_val):
        wb = xlrd.open_workbook("C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_4/data/datadriven.xlsx")
        ws = wb.sheet_by_name(Sheet_Name)
        row_count = ws.nrows
        col_count = ws.ncols
        for i in range(row_count):
            for j in range(col_count):
                if (ws.cell_value(i, j) == input_val):
                    val = ws.cell_value(i + 1, j)
            break
        return val

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def get_screenshot(self):
        cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        screenshot_name = "scr_" + cur_time
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(
            os.getcwd().replace("\\", "/").replace("pages","") + "/screenshots/" + screenshot_name + ".png")
        print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")








