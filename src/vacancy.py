import re


class Vacancy:
    """Класс для представления вакансии."""

    __slots__ = ("title", "url", "salary", "description", "id")

    def __init__(self, title: str, url: str, salary: dict | None, description: str | None, vacancy_id: str):
        self.id = vacancy_id
        self.title = title
        self.url = url
        self.salary = self._validate_salary(salary)
        self.description = description if description is not None else ""  # Заменяем None на пустую строку

    def _validate_salary(self, salary: dict | None) -> int:
        """Валидация зарплаты. Возвращает среднее значение между 'from' и 'to'."""
        if not salary:
            return 0
        salary_from = salary.get("from")
        salary_to = salary.get("to")
        if salary_from is not None and salary_to is not None:
            return (salary_from + salary_to) // 2
        elif salary_from is not None:  # Только нижняя граница
            return salary_from
        elif salary_to is not None:  # Только верхняя граница
            return salary_to
        else:
            return 0

    def __lt__(self, other) -> bool:
        return self.salary < other.salary

    def __gt__(self, other) -> bool:
        return self.salary > other.salary

    @classmethod
    def cast_to_object_list(cls, data: list[dict]) -> list["Vacancy"]:
        """Создаём список из JSON-данных."""

        # Список с вакансиями
        vacancies = []

        for item in data:
            # Очищаем описание от HTML-тегов
            raw_description = item.get("snippet", {}).get("requirement")
            clean_description = re.sub(r"<[^>]+>", "", raw_description) if raw_description else None

            vacancy = cls(
                title=item.get("name"),
                url=item.get("alternate_url"),
                salary=item.get("salary"),
                description=clean_description,  # Используем очищенное описание
                vacancy_id=item.get("id"),
            )
            vacancies.append(vacancy)
        return vacancies
