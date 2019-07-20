# # class A:
# #     def m1(self):
# #         print("in m1")
# #
# #
# # # a1 = A()
# # # a1.m1()
#
# def a():
#     try:
#         print("line 1")
#         assert 10==100
#         print("line 2")
#     except:
#         print("line 3")
#
# a()
import time

from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\\Users\\QSP\\PycharmProjects\\POM_Automation_7\\drivers\\chromedriver.exe")
driver.get("http://google.com")
driver.implicitly_wait(10)
driver.execute_script("window.alert('This is alert');")
time.sleep(5)
alert=driver.switch_to.alert
print(alert.text)
alert.dismiss()
#alert.accept()
driver.find_element_by_xpath("//input[@name='q']").send_keys("qspiders")



enter un["xpath","a","b"]
enter pwd[]
click on logn




# ele = driver.find_elements_by_xpath("//*[@jsname='aajZCb']//span/b")
# time.sleep(5)
# print(len(ele))
# for i in ele:
#     print(ele)















