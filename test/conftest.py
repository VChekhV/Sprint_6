import pytest
from selenium import webdriver
from pages.home_page import HomePageSamokat
from data_tests import BASE_URL


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get(BASE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def home_page(driver):
    home_page = HomePageSamokat(driver)
    home_page.close_cookie_window()
    return home_page

