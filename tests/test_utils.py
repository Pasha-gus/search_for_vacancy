from src.utils import filter_vacancy
from src.vacancy import Vacancy


def test_filter_vacancy(vacancy_data):
    vacancies = Vacancy.cast_to_object_list(vacancy_data)

    # Проверка фильтрации с нормальным количеством
    filtered_vacancies = filter_vacancy(vacancies, 5)
    assert len(filtered_vacancies) == 5

    # Проверка на правильность сортировки по зарплате
    salaries = [vacancy.salary_from for vacancy in filtered_vacancies]
    assert salaries == sorted(salaries, reverse=True)

    # Запрос большего количества вакансий, чем доступно
    filtered_vacancies = filter_vacancy(vacancies, 15)
    assert len(filtered_vacancies) == len(vacancies)

    # Запрос нуля вакансий
    filtered_vacancies = filter_vacancy(vacancies, 0)
    assert len(filtered_vacancies) == 0
    # Фильтрация с пустым списком вакансий
    empty_filtered_vacancies = filter_vacancy([], 5)
    assert len(empty_filtered_vacancies) == 0
