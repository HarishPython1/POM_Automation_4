import pytest
from pages.FB_LoginPage import FB_LoginPage

@pytest.mark.usefixtures("test_setup")
class  TestLogin:
    def test_login(self):
        driver=self.driver
        lp=FB_LoginPage(driver)
        lp.acti_login()