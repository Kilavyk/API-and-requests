from src.api import HeadHunterAPI
from src.vacancy import Vacancy
from src.saver import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies, filter_by_salary


def user_interaction():
    hh_api = HeadHunterAPI()
    json_saver = JSONSaver()

    search_query = input("Введите поисковый запрос: ")
    top_n = int(input("Введите количество вакансий для вывода: "))
    keywords = input("Введите ключевые слова через пробел: ").split()
    salary_range = input("Введите диапазон зарплат (например, 50000-100000): ")

    # Получение и сохранение вакансий
    hh_data = hh_api.get_vacancies(search_query)
    vacancies = Vacancy.cast_to_object_list(hh_data)
    for v in vacancies:
        json_saver.add_vacancy(v)

    # Фильтрация
    filtered = filter_vacancies(vacancies, keywords)
    salary_filtered = filter_by_salary(filtered, salary_range)
    sorted_vacs = sort_vacancies(salary_filtered)
    top_vacs = get_top_vacancies(sorted_vacs, top_n)

    print_vacancies(top_vacs)


if __name__ == "__main__":
    user_interaction()