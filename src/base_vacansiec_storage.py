from abc import ABC, abstractmethod
from src.vacancy import Vacancy


class VacancyStorage(ABC):
    """Абстрактный метод для сохранения вакансий в файл"""

    @abstractmethod
    def add_vacancy(self, list: Vacancy):
        """Сохоаняет вакансию в файл"""
        pass

    @abstractmethod
    def get_vacancies(self, criteria: list):
        """Получает вакансию по заданным критериям"""
        pass

    @abstractmethod
    def delete_vacancies(self):
        """Очищает файл с вакансиями"""
        pass
