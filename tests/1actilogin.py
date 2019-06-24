import pytest
from pages.LoginPage1 import LoginPage1

@pytest.mark.usefixtures("test_setup")
class  TestLogin1:
    def test_login1(self):
        driver = self.driver
        lp=LoginPage1(driver)
        lp.enter_un()
        lp.enter_pwd()
