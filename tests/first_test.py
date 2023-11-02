from pages import first_pages
from conftest import driver
from pages.first_pages import FirstPages


class TestFirstScenario:

    def test_steps_check_site(self, driver):
        first_page = FirstPages(driver, "https://sbis.ru")
        first_page.open()
        first_page.steps_check_site()

    def test_steps_check_photo(self, driver):
        first_page = FirstPages(driver, "https://tensor.ru")
        first_page.open()
        first_page.steps_check_photo()
