import pytest

from pages.FlipKartLoginPage import FBLoginPage


@pytest.mark.usefixtures("test_setup")
class TestFBLogin:
    @pytest.mark.parametrize("un,pwd", [("9538442585", "9538442585"), ("9538442585", "9538442585")])
    def test_login(self, un, pwd):
        driver = self.driver
        login_page = FBLoginPage(driver)
        login_page.fb_login(un, pwd)
