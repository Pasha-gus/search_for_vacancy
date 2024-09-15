from src.head_hunter_api import HeadHunterAPI
from src.utils import filter_vacancy
from src.vacanciec_storage import VacancyStorageJson
from src.vacancy import Vacancy


def main():
    api = HeadHunterAPI()
    query = input("Введите поисковой запрос: ")
    per_page = input("Ведите количество возращаемых результатов: ")
    vacancies_data = api.get_vacancies(query, per_page)
    vacancies_list = Vacancy.cast_to_object_list(vacancies_data)
    count = int(input("Введите количество вакансий для вывода в топ N: "))
    sorted_vacancy_by_salary = filter_vacancy(vacancies_list, count)
    path_to_file = input("Введите путь к файлу сохранения (Если нужно сохранить в файл по умолчанию нажмите Enter): ")
    if path_to_file:
        save_vacancions = VacancyStorageJson(path_to_file)
    else:
        save_vacancions = VacancyStorageJson()
    save_vacancions.add_vacancy(sorted_vacancy_by_salary)
    for vacancy in sorted_vacancy_by_salary:
        print(vacancy)


if __name__ == "__main__":
    main()
