import pytest
from src.vacancy import Vacancy


def test_vacancy_init(sample_vacancy):
    assert sample_vacancy.title == "Инженер-конструктор"
    assert sample_vacancy.url == "https://hh.ru/vacancy/111983655"
    assert sample_vacancy.salary == 160000  # (120000 + 200000) / 2
    assert sample_vacancy.description == "Требуется инженер с опытом работы"
    assert sample_vacancy.id == "111983655"


def test_vacancy_comparison(sample_vacancy):
    lower_vacancy = Vacancy("Test", "url", {"from": 50000, "to": 80000}, "desc", "2")
    higher_vacancy = Vacancy("Test", "url", {"from": 200000, "to": 300000}, "desc", "3")

    assert sample_vacancy > lower_vacancy
    assert sample_vacancy < higher_vacancy
    assert sample_vacancy != lower_vacancy


def test_cast_to_object_list(sample_vacancies_list):
    vacancies = Vacancy.cast_to_object_list(sample_vacancies_list)
    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].title == "Инженер-конструктор"
