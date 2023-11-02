from locators.locators import PageLocators as Locators
from pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
import time

class FirstPages(BasePage):

    def steps_check_site(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.element_is_visible(Locators.BANNER).click()

        # all_window_handles = self.driver.window_handles
        # self.driver.switch_to.window(all_window_handles[1])
        # self.wait_for_load()
        # with open('url.txt', 'w') as file:
        #     file.write(self.driver.current_url)
        self.check_current_url("https://tensor.ru")

        # Проверка блока Сила в людях
        #self.element_is_visible(Locators.PODROBNEE_BUTTON).click()
        # self.check_current_url("https://tensor.ru")
        # Проверка того что урл соответсвует
        # self.check_photo_size_equality()

    def steps_check_photo(self):
        self.element_is_visible(Locators.CLOSE_INTERCEPTOR).click()
        self.element_is_visible(Locators.PODROBNEE_BUTTON)
        self.check_photo_size_equality()

    # def find_elements_in_block(self):
    #     block_elements = self.elements_are_visible(Locators.BLOCK_ELEMENTS)
    #     block_elements[-1]




    def check_photo_size_equality(self):
        # Ожидаем видимости всех элементов PHOTO_LINK
        photo_elements = self.elements_are_visible(Locators.PHOTOS_LINK)

        # Получаем размер каждого элемента
        first_photo_size = photo_elements[0].size
        for element in photo_elements[1:]:
            assert element.size == first_photo_size, f"Фото с размером {element.size} не равно первому фото."
