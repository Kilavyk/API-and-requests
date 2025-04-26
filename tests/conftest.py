import pytest
from src.vacancy import Vacancy
from src.api import HeadHunterAPI
from src.saver import JSONSaver

@pytest.fixture
def sample_vacancy_data():
    return {
        "id": "111983655",
        "name": "Инженер-конструктор",
        "alternate_url": "https://hh.ru/vacancy/111983655",
        "salary": {
            "from": 120000,
            "to": 200000,
            "currency": "RUR",
            "gross": True
        },
        "snippet": {
            "requirement": "Требуется инженер с опытом работы"
        }
    }

@pytest.fixture
def sample_vacancy(sample_vacancy_data):
    return Vacancy(
        title=sample_vacancy_data["name"],
        url=sample_vacancy_data["alternate_url"],
        salary=sample_vacancy_data["salary"],
        description=sample_vacancy_data["snippet"]["requirement"],
        vacancy_id=sample_vacancy_data["id"]
    )

@pytest.fixture
def sample_vacancies_list(sample_vacancy_data):
    return [sample_vacancy_data]

@pytest.fixture
def hh_api():
    return HeadHunterAPI()

@pytest.fixture
def json_saver(tmp_path):
    return JSONSaver(filename=str(tmp_path / "test_vacancies.json"))