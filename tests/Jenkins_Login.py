import pytest

from pages.JenkinsLoginPage import JenkinsLoginPage
from pages.LoginPage1 import LoginPage1


@pytest.mark.usefixtures("test_setup")
class TestLogin1:
    def test_login(self):
        driver = self.driver
        lp = JenkinsLoginPage(driver)
        lp.jenkins_login()
