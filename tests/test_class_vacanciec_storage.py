from src.vacancy import Vacancy
import json


def test_add_vacancy(vac_storage):
    # Создаем некоторые вакансии, заполнив все необходимые параметры
    vacancies = [
        Vacancy(1, "Python Developer", "", 70000, 90000, "", "USD", "Remote"),
        Vacancy(2, "Data Scientist", "", 80000, 100000, "", "USD", "Remote"),
    ]

    # Добавляем вакансии
    vac_storage.add_vacancy(vacancies)

    # Проверяем, что вакансии были добавлены
    with open(vac_storage._VacancyStorageJson__file_name, "r") as f:
        data = json.load(f)
        assert len(data) == 2
        assert any(vacancy["name"] == "Python Developer" for vacancy in data)
        assert any(vacancy["name"] == "Data Scientist" for vacancy in data)


def test_get_vacancies(vac_storage):
    vacancies = [
        Vacancy(1, "Python Developer", "", 70000, 90000, "", "USD", "Remote"),
        Vacancy(2, "Java Developer", "", 70000, 90000, "", "USD", "Remote"),
    ]
    vac_storage.add_vacancy(vacancies)

    criteria = {"name": "Python"}
    found_vacancies = vac_storage.get_vacancies(criteria)

    assert len(found_vacancies) == 1
    assert found_vacancies[0]["name"] == "Python Developer"


def test_delete_vacancies(vac_storage):
    vacancies = [
        Vacancy(1, "Python Developer", "", 70000, 90000, "", "USD", "Remote"),
        Vacancy(2, "Data Scientist", "", 80000, 100000, "", "USD", "Remote"),
    ]
    vac_storage.add_vacancy(vacancies)

    # Удаляем все вакансии
    vac_storage.delete_vacancies()

    # Проверяем, что файл пуст
    with open(vac_storage._VacancyStorageJson__file_name, "r") as f:
        data = json.load(f)
        assert len(data) == 0
