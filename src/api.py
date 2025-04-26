from abc import ABC, abstractmethod
import requests


class JobPlatformAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass


class HeadHunterAPI(JobPlatformAPI):
    """Класс для работы с API hh.ru."""

    def __init__(self):
        self.url = 'https://api.hh.ru/vacancies'
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {
            'text': '',
            'search_field': 'name',
            'page': 0,
            'per_page': 100,
            'area': 113  # Код России в hh.ru
        }

    def _connect_to_api(self) -> requests.Response:
        """Приватный метод для подключения к API."""
        response = requests.get(self.url, headers=self.headers, params=self.params)
        if response.status_code != 200:
            raise Exception(f"Ошибка подключения: {response.status_code}")
        return response

    def get_vacancies(self, keyword: str) -> list[dict]:
        """Получить вакансии по ключевому слову."""
        self.params['text'] = keyword
        self.params['page'] = 0  # Сброс номера страницы
        vacancies = []

        while self.params['page'] < 5:  # Количество страниц для поиска, максимум 20
            response = self._connect_to_api()
            data = response.json()
            items = data.get('items', [])
            vacancies.extend(items)

            if not items:  # Если страница пустая, прерываем цикл
                break

            self.params['page'] += 1

        return vacancies
