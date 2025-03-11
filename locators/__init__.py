import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.home_page_locators import TestHomePageLocators
from pages.base_page import BasePage
from data_tests import DZEN_URL

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def click_logo_yandex_open_dzen_page(self):
        self.driver.find_element(*self.LOGO_YANDEX).click()
        # Переключение на новую вкладку
        self.driver.switch_to.window(self.driver.window_handles[1])

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_original_tab(self):
        # Переключение обратно на исходную вкладку
        self.driver.switch_to.window(self.driver.window_handles[0])

    def click_logo_open_home_page(self):
        self.driver.find_element(*self.LOGO_SAMOKAT).click()

class HomePageSamokat(BasePage):

    @allure.step('Нажатие кнопки "Заказать" в хедере')