import pytest
from unittest.mock import patch, Mock
from src.api import HeadHunterAPI


def test_api_init(hh_api):
    assert hh_api.url == "https://api.hh.ru/vacancies"
    assert hh_api.headers == {"User-Agent": "HH-User-Agent"}
    assert hh_api.params["per_page"] == 100


@patch("requests.get")
def test_get_vacancies_success(mock_get, hh_api, sample_vacancies_list):
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.json.return_value = {"items": sample_vacancies_list}
    mock_get.return_value = mock_response

    vacancies = hh_api.get_vacancies("инженер")
    assert len(vacancies) == 5
    assert vacancies[0]["name"] == "Инженер-конструктор"


@patch("requests.get")
def test_api_connection_error(mock_get, hh_api):
    mock_response = Mock()
    mock_response.status_code = 500
    mock_get.return_value = mock_response

    with pytest.raises(Exception, match="Ошибка подключения: 500"):
        hh_api._connect_to_api()