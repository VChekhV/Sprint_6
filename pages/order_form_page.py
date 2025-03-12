import allure

class OrderFormPage(BasePage):
    @allure.step('Заполнить поле "Имя"')
    def set_first_name(self, name):
        self.set_text_to_elm(TestOrderFormPageLocators.FIRST_NAME_FIELD, name)
        return self

    @allure.step('Проверка, что поле "Имя" содержит значение')
    def check_first_name_value(self, expected_value):

    @allure.step('Заполнить поле "Фамилия"')

    def set_last_name(self, last_name):
        self.set_text_to_elm(TestOrderFormPageLocators.LAST_NAME_FIELD, last_name)
        return self

    @allure.step('Заполнить поле "Адрес"')
    def set_address(self, address):
        self.set_text_to_elm(TestOrderFormPageLocators.ADDRESS_FIELD, address)
        return self

    @allure.step('Заполнить поле "Метро"')
    def set_metro(self, station):
        self.click_on_element(TestOrderFormPageLocators.METRO_STATION_FIELD)
        self.set_text_to_elm(TestOrderFormPageLocators.METRO_STATION_FIELD, station)
        self.click_on_element(TestOrderFormPageLocators.SELECTED_STATION)
        return self

    def check_metro_value(self, station):
        field = self.find_element_with_wait(TestOrderFormPageLocators.METRO_STATION_FIELD)


    def check_metro_value(self, station):
    @allure.step('Заполнить поле "Телефон"')
    def set_phone(self, number):
        self.set_text_to_elm(TestOrderFormPageLocators.PHONE_NUMBER_FIELD, number)
        return self

    @allure.step('Нажать кнопку "Далее"')
    def click_next_button(self):

    def set_rental_date(self):
        today = self.find_element_with_wait(TestOrderFormPageLocators.TODAY_DATE_CALENDAR)
        tomorrow = today.find_element(*TestOrderFormPageLocators.TOMORROW_DATE_CALENDAR)
        tomorrow.click()
        return self

    @allure.step('Заполнить поле "Срок аренды"')
    def set_rental_duration(self):
        self.click_on_element(TestOrderFormPageLocators.RENTAL_DURATION_FIELD)
        self.find_element_with_wait(TestOrderFormPageLocators.RENTAL_DURATION_LIST)
        self.click_on_element(TestOrderFormPageLocators.DROPDOWN_ITEM_RENTAL_PERIOD)

    def set_color_field(self):
        self.click_on_element(TestOrderFormPageLocators.CHECKBOX_GREY)
        return self

    def set_comment_field(self, comment):
        self.set_text_to_elm(TestOrderFormPageLocators.COMMENT_FIELD, comment)
        return self

    @allure.step('Нажать кнопку "Заказать"')
    def click_order_button(self):
    def check_displaying_of_confirm_window(self):
    def click_yes_button_confirmation_pop_up(self):
        self.click_on_element(TestOrderFormPageLocators.YES_BUTTON_POP_UP_CONFIRM_ORDER)
        self.find_element_with_wait(TestOrderFormPageLocators.POP_UP_COMPLETE_ORDER)
        return self

    @allure.step('Заполнение первой части формы и нажатие кнопки "Далее"')
    def personal_information_input(self, name, last_name, address, station, number):