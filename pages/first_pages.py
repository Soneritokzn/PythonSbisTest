from selenium.webdriver import ActionChains

from locators.locators import PageLocators as Locators
from pages.base_page import BasePage


class FirstPages(BasePage):

    def steps_check_site(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.element_is_visible(Locators.BANNER).click()
        self.check_sila_button()
        self.check_current_url("https://tensor.ru")

    def steps_check_photo(self):
        self.element_is_visible(Locators.CLOSE_INTERCEPTOR).click()
        self.driver.get("https://tensor.ru/about")
        element = self.elements_are_collected(Locators.PHOTOS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()
        self.check_photo_size_equality()

    def check_photo_size_equality(self):
        photo_elements = self.elements_are_visible(Locators.PHOTOS_LINK)

        first_photo_size = photo_elements[0].size
        for element in photo_elements[1:]:
            assert element.size == first_photo_size, f"Фото с размером {element.size} не равно первому фото."

    def check_sila_button(self):
        sila_button = self.element_is_visible(Locators.SILA_V_LUDAH_BUTTON)
        assert sila_button, "Блок 'Сила в людях' не найден на странице."
