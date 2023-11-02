import pytest
from pages.second_page import SecondPages
from conftest import driver

class TestSecondScenario:

    def test_check_right_region(self, driver):
        second_page = SecondPages(driver, "https://sbis.ru")
        second_page.open()
        second_page.define_region()



    def test_change_and_check_region(self, driver):
        second_page = SecondPages(driver, "https://sbis.ru")
        second_page.open()
        second_page.change_region()
