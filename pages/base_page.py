from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    def open(self):
        self.driver.get(self.url)

    def element_is_visible(self, locator, timeout=40):
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def elements_are_visible(self, locator, timeout=30):
        return Wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    def elements_are_collected(self, locator, timeout=40):
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def window_switcher(self, expected_url):
        main_window_handle = self.driver.current_window_handle

        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
            if expected_url in self.driver.current_url:
                return

        self.driver.switch_to.window(main_window_handle)

    def check_current_url(self, expected_url):
        current_url = self.driver.current_url
        assert current_url == expected_url, f"Текущий URL {current_url} не соответствует ожидаемому URL {expected_url}"

    def element_is_invisible(self, locator, timeout=10):
        return Wait(self.driver, timeout).until(EC.invisibility_of_element_located(locator))

    def wait_for_load(self):
        WebDriverWait(self.driver, 40).until(EC.url_to_be("https://tensor.ru"))



