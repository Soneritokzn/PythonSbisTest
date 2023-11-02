from selenium.webdriver.common.by import By


class PageLocators:
    CONTACTS_LINK = (By.LINK_TEXT, "Контакты")
    BANNER = (By.XPATH, '//img[@alt="Разработчик системы СБИС — компания «Тензор»"]')
    TENSOR_LOGO = (By.CSS_SELECTOR, "a.sbtsru-Contacts__logo-tensor img[alt='Разработчик системы СБИС — компания "
                                    "«Тензор»']")

    CLOSE_INTERCEPTOR = (By.CLASS_NAME, "tensor_ru-CookieAgreement__close")
    CLOSE_SECOND_INTERCEPTOR = (By.CSS_SELECTOR, ".sbisru-Header__...")
    SILA_V_LUDAH_BUTTON = (By.CLASS_NAME, "tensor_ru-Index__card-title")
    PODROBNEE_BUTTON = (By.CSS_SELECTOR, "div.tensor_ru-Index__block4-content > p.tensor_ru-Index__card-text > "
                                         "a.tensor_ru-link")
    RABOTAEM_LINK = (By.LINK_TEXT, "Rabotaem")
    PHOTOS_LINK = (By.CSS_SELECTOR, ".tensor_ru-About__block3-image.new_lazy.loaded")  # Здесь группа из четырех
    # изображений

    REGION_NAME = (By.CLASS_NAME, "sbis_ru-Region-Chooser__text")  # Проверка региона туда же клик
    PARTNERS_LINK = (By.XPATH, '//*[@id="contacts_list"]/div/div[2]')  # Проверка партнера
    REGION_CHOICE = (By.XPATH, '//span[@title="Камчатский край" and text()="41 Камчатский край"]')  # Выбор региона
    REGION_NAME_UPDATED = (
        By.XPATH, '//span[@class="sbis_ru-Region-Chooser__text" and text()="Камчатский край"]')  # Новое имя региона
    PARTNERS_LINK_UPDATED = (By.XPATH, '//div[@class="sbisru-Contacts-List__city" and text('
                                       ')="Петропавловск-Камчатский"]')  # Обновленный партнер проверка
    NEW_URL = "https://sbis.ru/contacts/41-kamchatskij-kraj?tab=clients"
