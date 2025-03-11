from data_tests import user_1, user_2

class TestOrderForm:
    @staticmethod
    def order_page(driver):
        order_page = OrderFormPage(driver)
        return order_page

    @allure.title('Проверка флоу позитивного сценария оформления заказа посредством верхней кнопки "Заказать')
    @allure.description('Проверка перехода в форму заказа через нажатие кнопки "Заказать" в хедере и успешного оформления заказа')