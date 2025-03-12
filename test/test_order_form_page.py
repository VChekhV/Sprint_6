import allure
import pytest
from data_tests import user_1, user_2

class TestOrderForm:
    @staticmethod
    def order_page(driver):
        order_page = OrderFormPage(driver)
        return order_page

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством верхней кнопки "Заказать"')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в хедере и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_1])
    def test_complete_order_form_order_button_header(self, driver, home_page, order_page, name, last_name, address, station, number, comment):
        home_page.click_order_button_header()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.is_pop_up_complete_order_displayed(), "Попап успешного оформления заказа не отображается"

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством нижней кнопки "Заказать"')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в теле и успешного оформления заказа')
    @pytest.mark.parametrize('name, last_name, address, station, number, comment', [user_2])
    def test_complete_order_form_order_button_body(self, driver, home_page, order_page, name, last_name, address, station, number, comment):
        home_page.click_order_button_body()
        order_page.personal_information_input(name, last_name, address, station, number)
        order_page.rental_information_input(comment)
        order_page.click_yes_button_confirmation_pop_up()
        assert order_page.is_pop_up_complete_order_displayed(), "Попап успешного оформления заказа не отображается"