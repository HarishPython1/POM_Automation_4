import allure
from selenium.common.exceptions import *
import xlrd
import os
import moment
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


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
        return ele

    def mul_locator(self, loc_type, locator_val):
        try:
            if loc_type == "name":
                ele = self.driver.find_elements_by_name(locator_val)
            elif loc_type == "id":
                ele = self.driver.find_elements_by_id(locator_val)
            elif loc_type == "xpath":
                ele = self.driver.find_elements_by_xpath(locator_val)
            elif loc_type == "tagname":
                ele = self.driver.find_elements_by_tag_name(locator_val)
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
        return ele

    def wait_ele_to_be_visible(self, loc_type, locator_val):
        if loc_type == "xpath":
            wait = WebDriverWait(self.driver, 10)
            wait.until(
                EC.visibility_of_element_located(By.XPATH, locator_val))

    def accept_alert(self):
        try:
            a=self.driver.switch_to.alert()
            a.accept()
        except NoAlertPresentException:
            return False

    def dismiss_alert(self):
        try:
            a=self.driver.switch_to.alert()
            a.dismiss()
        except NoAlertPresentException:
            return False

    def get_val(self, sheet_name, input_val):
        wb = xlrd.open_workbook("C:/Users/BTM-Faculty/PycharmProjects/POM_Automation_4/data/datadriven.xlsx")
        ws = wb.sheet_by_name(sheet_name)
        row_count = ws.nrows
        col_count = ws.ncols
        for i in range(row_count):
            for j in range(col_count):
                if ws.cell_value(i, j) == input_val:
                    val = ws.cell_value(i + 1, j)
            break
        return val

    def delete_cookies(self):
        self.driver.delete_all_cookies()

    def key_escape(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ESCAPE)

    def validate_title(self,expected_res):
        val = self.driver.title#app
        assert val == expected_res

    def validate_SuccMessage(self,expected_res):
        val = self.driver.title#app>>text
        assert val == expected_res

    def get_screenshot(self, log):
        cur_time = moment.now().strftime("%d-%m-%Y_%H-%M-%S")
        screenshot_name = log + "  " + cur_time
        allure.attach(self.driver.get_screenshot_as_png(), name=screenshot_name,
                      attachment_type=allure.attachment_type.PNG)
        self.driver.get_screenshot_as_file(
            os.getcwd().replace("\\", "/").replace("pages", "") + "/screenshots/" + screenshot_name + ".png")
        print(os.getcwd().replace("\\", "/").replace("tests", "screenshots") + "/" + screenshot_name + ".png")
