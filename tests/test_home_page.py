class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def click_on_element(self, locator):
        element = self.driver.find_element(*locator)
        element.click()

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_original_tab(self):
        original_window = self.driver.window_handles[0]
        self.driver.switch_to.window(original_window)

    def scroll_to_faq(self):
        pass

import allure
import pytest

    @allure.title('Проверка раздела "Вопросы о важном"')
    @allure.description('Проверка появления соответствующего текста ответа при нажатии на каждый вопрос')
    @pytest.mark.parametrize('question_locator, answer_locator, expected_text', [
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_1, TestHomePageLocators.ANSWER_FAQ_1, expected_texts['faq1']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_6, TestHomePageLocators.ANSWER_FAQ_6, expected_texts['faq6']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_7, TestHomePageLocators.ANSWER_FAQ_7, expected_texts['faq7']),
        (TestHomePageLocators.ACCORDION_BUTTON_FAQ_8, TestHomePageLocators.ANSWER_FAQ_8, expected_texts['faq8'])
    ])
    def test_click_question_shows_answer_faq(self, driver, home_page, question_locator, answer_locator, expected_text):
        home_page.scroll_to_faq()
        home_page.click_on_element(question_locator)  # заменяем на метод из BasePage

    @allure.description('Проверка открытия страницы Яндекс.Дзен в соседней вкладке при нажатии на логотип "Яндекс"')
    def test_clicking_yandex_logo_opens_dzen_page(self, driver, home_page):
        home_page.click_logo_yandex_open_dzen_page()  # Предполагается, что этот метод тоже реализован в BasePage
        assert home_page.get_current_url() == DZEN_URL  # заменяем вызов драйвера на метод из BasePage
        home_page.switch_to_original_tab()  # используем метод из BasePage

    @allure.title('Проверка нажатия на логотип "Самокат"')
    @allure.description('Проверка перехода на главную страницу при нажатии на логотип "Самокат"')
    def test_click_logo_samokat_open_home_page(self, driver, home_page):
        home_page.click_order_button_header()
        home_page.click_logo_open_home_page()  # используем метод из BasePage
        assert home_page.get_current_url() == BASE_URL  # заменяем вызов драйвера на метод из BasePage