from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import PageLocators as Locators


class SecondPages(BasePage):

    def define_region(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.check_region("г. Москва")
        self.element_is_visible(Locators.REGION_NAME).click()
        self.element_is_visible(Locators.REGION_CHOICE).click()






    def change_region(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.element_is_visible(Locators.REGION_NAME).click()
        self.element_is_visible(Locators.REGION_CHOICE).click()


    def check_region(self, expected_region):
        region_name_element = self.element_is_visible(Locators.REGION_NAME)
        region_name = region_name_element.find_element(By.XPATH,'//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div[2]/span/span').text
        assert region_name == expected_region, f"Регион не соответствует ожидаемому. Ожидался {expected_region}, фактический: {region_name}"

    # 1) Перейти
    # на
    # https: // sbis.ru / в
    # раздел
    # "Контакты"
    # 2) Проверить, что
    # определился
    # ваш
    # регион(в
    # нашем
    # примере
    # Ярославская
    # обл.) и
    # есть
    # список
    # партнеров.

    # 3) Изменить
    # регион
    # на
    # Камчатский
    # край
    # 4) Проверить, что
    # подставился
    # выбранный
    # регион, список
    # партнеров
    # изменился, url
    # и
    # title
    # содержат
    # информацию
    # выбранного
    # региона
