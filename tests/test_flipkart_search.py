import time

import pytest

from pages.FlipKartDashBoardPage import FBDashBoardPage
from pages.FlipKartLoginPage import FBLoginPage


@pytest.mark.usefixtures("test_setup")
class TestFBSearch:
   # @pytest.mark.parametrize("un,pwd", [("test", "testpwd")])
    @pytest.mark.smoke
    def test_login(self):
        driver = self.driver
        login_page = FBLoginPage(driver)
        login_page.fb_close()
        dashboard_page = FBDashBoardPage(driver)
        dashboard_page.validate_title(
            "Online Shopping Site for Mobiles, Electronics, Furniture, Grocery, Lifestyle, Books & More. Best Offers!")
        dashboard_page.fb_search("android")
        dashboard_page.fb_click_on_search()



