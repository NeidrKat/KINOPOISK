import pytest
import requests
import allure
from config import url_API, HEADERS


@allure.feature('API Responses')
@pytest.mark.parametrize("endpoint, expected_status", [
    # Possitive_test
    ("/movie/301", 200),
    ("/movie/search?page=1&limit=10&query=Лобстер", 200),
    ("/person/search?page=1&limit=10&query=Стэйтем", 200),
    # Negative_test
    ("/movie/search?page=0&limit=0&query=Лобстер", 400),
    ("/movie/1000000000000", 400)
    ])
def test_api_responses(endpoint, expected_status):
    """
    Универсальный тест для проверки статуса ответа"
    "API по различным endpoint'ам.
    """
    with allure.step(f"Отправка GET запроса на {endpoint}"):
        response = requests.get(f"{url_API}{endpoint}", headers=HEADERS)

    with allure.step(f"Проверка, что статус ответа равен {expected_status}"):
        assert response.status_code == expected_status, f"Expected {expected_status}, got {response.status_code}"
