from abc import ABC, abstractmethod


class JobPlatformAPI(ABC):
    """Абстрактный класс для работы с API."""

    @abstractmethod
    def get_vacancies(self, keyword: str) -> list[dict]:
        pass


