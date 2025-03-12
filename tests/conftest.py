import pytest
from selenium import webdriver
from pages.home_page import HomePage
from pages.home_page import HomePageSamokat
from pages.order_form_page import OrderFormPage
from data_tests import BASE_URL


def home_page(driver):
    home_page.close_cookie_window()
    return home_page


@pytest.fixture
def order_page(driver):
    order_page = OrderFormPage(driver)
    return order_page