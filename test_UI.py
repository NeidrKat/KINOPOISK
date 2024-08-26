import pytest
import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
from SearchPage import SearchPage
from config import url_UI


@pytest.fixture(scope='session')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def search_page(driver):
    driver.get(url_UI)
    return SearchPage(driver)


@allure.feature('поиск по названию фильма')
def test_search_by_title(search_page):
    """
    Тест UI. Поиск по названию фильма
    """
    with allure.step("Поиск контента по названию 'Дьявол в деталях'"):
        search_page.search_by_title("Дьявол в деталях")

    with allure.step("Проверка, что найденный "
                     " контент соответствует фильму 'The Little Things'"):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "The Little Things")
        assert is_content_found, "Expected "
        "to find content 'The Little Things'"


@allure.feature('поиск по году')
def test_search_year(search_page):
    with allure.step("Поиск контента с годом выпуска '2020'"):
        search_page.search_by_year("2020")

    with allure.step("Проверка, что найденный контент "
                     "содержит искомый год'2020'"):
        is_years_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, 'year', '2020')
    assert is_years_found, "Expected to find content '2020'"


@allure.feature('поиск по жанру')
def test_search_by_genre(search_page):
    """
    Тест UI. Поиск по жанру фильма
    """
    with allure.step("Поиск контента по жанру 'детектив'"):
        search_page.search_by_genre("детектив")

    with allure.step("Проверка, что найденное относится к жанру 'детектив'"):
        is_genre_found = search_page.wait_for_element_with_text(
            By.XPATH, "//span[@class='gray' and contains(., 'детектив')]",
            "детектив")
        assert is_genre_found, "Expected to find content with genre 'детектив'"


@allure.feature('Поиск по названию и актеру')
def test_search_by_actor_and_name(search_page):
    """
    Тест UI. Поиск по названию и актеру
    """
    with allure.step("Поиск контента по названию 'Начало'"
                     "и актеру 'Леонардо'"):
        search_page.search_by_actor_and_name("Леонардо", "Начало")

    with allure.step("Проверка, что найденный контент "
                     "соответствует фильму 'Inception, 148 мин' "
                     "с актером 'Леонардо'"):
        is_content_found = search_page.wait_for_element_with_text(
            By.CLASS_NAME, "gray", "Inception, 148 мин")
        assert is_content_found, "Expected to find content\
            'Inception, 148 мин'"


@allure.feature('Поиск по стране')
def test_search_by_country(search_page):
    """
    Тест UI на поиск контента по стране.
    """
    with allure.step("Поиск контента по стране 'Лаос'"):
        search_page.search_by_country("Лаос")

    with allure.step("Проверка, что найденный контент "
                     "соответствует стране 'Лаос'"):
        country = search_page.wait_for_element(
            By.CLASS_NAME, "text-blue")
        assert country.text == "«Лаос»", f"Expected country \
            to be '«Лаос»', but got {country.text}"
