import pytest

from pages.DragDemo import DragPage


@pytest.mark.usefixtures("test_setup")
class  TestDragAndDrop:
    def test_drag_and_drop(self):
        driver=self.driver
        ddemo=DragPage(driver)
        ddemo.jquery_drag()
