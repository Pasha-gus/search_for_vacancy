from src.base_vacansiec_storage import VacancyStorage
import os
import json
from src.vacancy import Vacancy
from src.utils import vacancy_to_dict
from typing import List


class VacancyStorageJson(VacancyStorage):
    def __init__(
        self,
        file_name: str = os.path.join(
            os.path.abspath(os.path.dirname(__file__)), "..", "data", "vacancy_storage.json"
        ),
    ):
        self.__file_name = file_name  # Приватный атрибут
        if not os.path.isfile(self.__file_name):
            with open(self.__file_name, "w") as f:
                json.dump([], f)

    def add_vacancy(self, vacancies: List[Vacancy]):
        """Сохраняет вакансии в файл, избегая дубликатов"""
        dict_vacancies = vacancy_to_dict(vacancies)
        try:
            with open(self.__file_name, "r") as f:
                existing_vacancies = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            existing_vacancies = []

        existing_vacancy_names = {vacancy["name"] for vacancy in existing_vacancies}

        new_vacancies = [vacancy for vacancy in dict_vacancies if vacancy["name"] not in existing_vacancy_names]
        existing_vacancies.extend(new_vacancies)

        try:
            with open(self.__file_name, "w") as f:
                json.dump(existing_vacancies, f, indent=4)
        except IOError as e:
            print(f"Ошибка записи в файл: {e}")

    def get_vacancies(self, criteria: dict):
        """Ищет вакансии по заданному критерию"""
        with open(self.__file_name, "r") as f:
            vacancies = json.load(f)

        result = []
        search_terms = []
        for value in criteria.values():
            search_terms.extend(value.lower().split())

        for vacancy in vacancies:
            if any(term in vacancy["name"].lower() for term in search_terms):
                result.append(vacancy)

        return result

    def delete_vacancies(self):
        """Очищает файл с вакансиями"""
        with open(self.__file_name, "w") as f:
            json.dump([], f)
