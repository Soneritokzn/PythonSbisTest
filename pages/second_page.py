from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from locators.locators import PageLocators as Locators


class SecondPages(BasePage):

    def define_region(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.check_region("г. Москва")
        self.check_partners_list()


    def change_region(self):
        self.element_is_visible(Locators.CONTACTS_LINK).click()
        self.element_is_visible(Locators.REGION_NAME).click()
        self.element_is_visible(Locators.REGION_CHOICE).click()
        self.check_region("Камчатский край")
        self.check_partners_list()
        self.check_region_info()

    def check_region(self, expected_region):
        region_name_element = self.element_is_visible(Locators.REGION_NAME)
        region_name = region_name_element.find_element(By.XPATH,
                                                       '//*[@id="container"]/div[1]/div/div[3]/div[2]/div[1]/div/div['
                                                       '2]/span/span').text
        assert region_name == expected_region, f"Регион не соответствует ожидаемому. Ожидался {expected_region}, " \
                                               f"фактический: {region_name} "




    def check_partners_list(self):
        partners_list = self.element_is_visible(Locators.PARTNERS_LINK)
        assert partners_list is not None, "Список партнеров не найден на странице"

    def check_region_info(self):
        expected_region = "kamchatskij-kraj"
        expected_title = "Камчатский край"
        current_url = self.driver.current_url
        current_title = self.driver.title
        assert expected_region in current_url, f"URL не содержит информацию о регионе: {current_url}"
        assert expected_title in current_title, f"Title не содержит информацию о регионе: {current_title}"


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
