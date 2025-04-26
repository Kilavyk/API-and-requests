import json
from abc import ABC, abstractmethod
from pathlib import Path

from src.vacancy import Vacancy


class Saver(ABC):
    """Абстрактный класс для работы с файлами."""

    @abstractmethod
    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: dict) -> list[dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: 'Vacancy') -> None:
        pass


class JSONSaver(Saver):
    """Класс для сохранения в JSON."""

    def __init__(self, filename: str = 'vacancies.json'):
        self.filename = Path('data') / filename
        self._ensure_dir()

    def _ensure_dir(self) -> None:
        """Создать папку data, если её нет."""
        self.filename.parent.mkdir(exist_ok=True)

    def add_vacancy(self, vacancy: 'Vacancy') -> None:
        """Добавить вакансию в файл."""
        data = []
        if self.filename.exists():
            data = json.loads(self.filename.read_text(encoding='utf-8'))

        vacancy_dict = {
            'id': vacancy.id,
            'title': vacancy.title,
            'url': vacancy.url,
            'salary': vacancy.salary,
            'description': vacancy.description
        }

        if not any(v['id'] == vacancy.id for v in data):
            data.append(vacancy_dict)
            self.filename.write_text(
                json.dumps(data, ensure_ascii=False, indent=4),
                encoding='utf-8'
            )

    def get_vacancies(self, criteria: dict) -> list[dict]:
        """Получает вакансии, соответствующие всем указанным критериям поиска."""

        # Загружаем данные из JSON-файла
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                all_vacancies = json.load(file)
        except Exception as e:
            print(f"Ошибка при чтении файла: {e}")
            return []

        # Список для подходящих вакансий
        suitable_vacancies = []

        # Проверяем каждую вакансию
        for vacancy in all_vacancies:
            meets_all_criteria = self._check_vacancy_criteria(vacancy, criteria)
            if meets_all_criteria:
                suitable_vacancies.append(vacancy)

        return suitable_vacancies

    def _check_vacancy_criteria(self, vacancy: dict, criteria: dict) -> bool:
        """Проверяет, соответствует ли вакансия всем критериям поиска."""
        for field, expected_value in criteria.items():
            actual_value = vacancy.get(field)
            if actual_value != expected_value:
                return False
        return True

    def delete_vacancy(self, vacancy: 'Vacancy') -> None:
        """Удалить вакансию из файла."""
        try:
            # Чтение и загрузка данных из файла
            with open(self.filename, 'r', encoding='utf-8') as file:
                vacancies = json.load(file)

            # Фильтрация вакансий - исключаем удаляемую
            updated_vacancies = [
                v for v in vacancies
                if v['id'] != vacancy.id
            ]

            # Если количество не изменилось - вакансия не найдена
            if len(updated_vacancies) == len(vacancies):
                print(f"Вакансия с ID {vacancy.id} не найдена.")
                return

            # Запись обновленных данных в файл
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(
                    updated_vacancies,
                    file,
                    ensure_ascii=False,
                    indent=2
                )

        except json.JSONDecodeError as e:
            print(f"Ошибка чтения JSON: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")
