import pytest
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, filter_by_salary
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Программист", "url1", {"from": 50000, "to": 80000}, "Python разработчик", "1"),
        Vacancy("Менеджер", "url2", {"from": 200000, "to": 300000}, "Управление проектами", "2"),
        Vacancy("Инженер", "url3", {"from": 120000, "to": 200000}, "Инженерные системы", "3")
    ]

def test_filter_vacancies(sample_vacancies):
    filtered = filter_vacancies(sample_vacancies, ["python"])
    assert len(filtered) == 1
    assert filtered[0].title == "Программист"

def test_sort_vacancies(sample_vacancies):
    sorted_vac = sort_vacancies(sample_vacancies)
    assert sorted_vac[0].title == "Менеджер"
    assert sorted_vac[1].title == "Инженер"
    assert sorted_vac[2].title == "Программист"

def test_get_top_vacancies(sample_vacancies):
    top = get_top_vacancies(sample_vacancies, 2)
    assert len(top) == 2
    assert top[0].title == "Программист"

def test_filter_by_salary(sample_vacancies):
    filtered = filter_by_salary(sample_vacancies, "100000-250000")
    assert len(filtered) == 2
    assert filtered[0].title == "Менеджер"
    assert filtered[1].title == "Инженер"