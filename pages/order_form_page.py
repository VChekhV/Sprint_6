# pages/order_form_page.py

from selenium.webdriver.remote.webdriver import WebDriver
from locators.order_form_page_locators import TestOrderFormPageLocators

class OrderFormPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def personal_information_input(self, name, last_name, address, station, number):
        # Заполнение личной информации
        self.driver.find_element(*TestOrderFormPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*TestOrderFormPageLocators.LAST_NAME_INPUT).send_keys(last_name)
        self.driver.find_element(*TestOrderFormPageLocators.ADDRESS_INPUT).send_keys(address)
        self.driver.find_element(*TestOrderFormPageLocators.STATION_INPUT).send_keys(station)
        self.driver.find_element(*TestOrderFormPageLocators.NUMBER_INPUT).send_keys(number)

    def rental_information_input(self, comment):
        # Заполнение информации об аренде
        self.driver.find_element(*TestOrderFormPageLocators.COMMENT_INPUT).send_keys(comment)

    def click_yes_button_confirmation_pop_up(self):
        # Нажатие кнопки "Да" в попапе подтверждения
        self.driver.find_element(*TestOrderFormPageLocators.YES_BUTTON).click()

    def is_pop_up_complete_order_displayed(self):
        # Проверка, отображается ли попап успешного оформления заказа
        return self.driver.find_element(*TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER).is_displayed()