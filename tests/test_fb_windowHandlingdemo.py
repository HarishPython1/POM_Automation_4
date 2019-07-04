import pytest

from pages.WindowHadnlingDemo import WindowHandlingPage


@pytest.mark.usefixtures("test_setup")
class  TestWindowHandling:
    def test_window_handling(self):
        driver=self.driver
        dd=WindowHandlingPage(driver)
        dd.window_handle()