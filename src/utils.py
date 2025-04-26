from src.vacancy import Vacancy


def filter_vacancies(vacancies: list[Vacancy], keywords: list[str]) -> list[Vacancy]:
    """Фильтровать вакансии по ключевым словам."""

    # Список для подходящих вакансий
    filtered_vacancies = []

    # Приводим к нижнему регистру
    normalized_keywords = [kw.lower() for kw in keywords]

    for vacancy in vacancies:
        description = vacancy.description or ""
        normalized_description = description.lower()

        # Проверяем каждое ключевое слово
        for keyword in normalized_keywords:
            if keyword in normalized_description:
                filtered_vacancies.append(vacancy)
                break

    return filtered_vacancies

def sort_vacancies(vacancies: list[Vacancy]) -> list[Vacancy]:
    """Сортировать вакансии по зарплате."""
    return sorted(vacancies, reverse=True)

def get_top_vacancies(vacancies: list[Vacancy], top_n: int) -> list[Vacancy]:
    """Вернуть топ N вакансий."""
    return vacancies[:top_n]

def print_vacancies(vacancies: list[Vacancy]) -> None:
    """Формируем и выводим список вакансий."""
    for v in vacancies:
        print(
            f"\nНазвание: {v.title}\n"
            f"Зарплата: {v.salary if v.salary else 'Не указана'}\n"
            f"Описание: {v.description[:125] + '...' if v.description else 'Нет описания'}\n"
            f"Ссылка: {v.url}\n"
            f"{'-' * 50}"
        )

def filter_by_salary(vacancies: list[Vacancy], salary_range: str) -> list[Vacancy]:
    """Фильтрует вакансии по диапазону зарплат. Формат: '100000-150000'"""
    try:
        min_s, max_s = map(int, salary_range.split('-'))
        return [v for v in vacancies if min_s <= v.salary <= max_s]
    except (ValueError, AttributeError):
        return vacancies  # Если ввод некорректен, возвращаем все вакансии