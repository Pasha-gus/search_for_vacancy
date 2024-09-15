from src.vacancy import Vacancy
from typing import List


def vacancy_to_dict(vacancies: List[Vacancy]) -> list:
    """Преобразует список объектов класса Vacancy в список словарей"""
    result = []
    for vacancy in vacancies:
        vacancy_dict = {
            "id": vacancy.id,
            "name": vacancy.name,
            "salary_from": vacancy.salary_from,
            "salary_to": vacancy.salary_to,
            "currency": vacancy.currency,
            "location": vacancy.location,
            "description": vacancy.description,
        }
        result.append(vacancy_dict)
    return result


def filter_vacancy(vacancies: List[Vacancy], n: int) -> List[Vacancy]:
    """Функция принимает список вакансий и количество возвращаемых вакансий, и возвращает список, отфильтрованный по минимальной зарплате"""
    sorted_vacancies = sorted(vacancies, key=lambda x: x.salary_from, reverse=True)
    return sorted_vacancies[:n]
