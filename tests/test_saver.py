import json

import pytest

from src.saver import JSONSaver


def test_json_saver_init(json_saver):
    assert json_saver.filename.name == "test_vacancies.json"


def test_add_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)

    with open(json_saver.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 1
        assert data[0]["title"] == "Инженер-конструктор"


def test_get_vacancies(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)

    result = json_saver.get_vacancies({"title": "Инженер-конструктор"})
    assert len(result) == 1

    result = json_saver.get_vacancies({"title": "Несуществующая вакансия"})
    assert len(result) == 0


def test_delete_vacancy(json_saver, sample_vacancy):
    json_saver.add_vacancy(sample_vacancy)
    json_saver.delete_vacancy(sample_vacancy)

    with open(json_saver.filename, "r", encoding="utf-8") as f:
        data = json.load(f)
        assert len(data) == 0
