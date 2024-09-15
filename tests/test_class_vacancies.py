from src.vacancy import Vacancy
import pytest

from src.vacancy import Vacancy
import pytest


def test_valid_vacancy_creation():
    vacancy = Vacancy(
        "1",
        "Разработчик",
        "http://example.com/job/1",
        50000,
        70000,
        "Ищем квалифицированного разработчика.",
        "RUB",
        "Москва",
    )

    assert vacancy.id == "1"
    assert vacancy.name == "Разработчик"
    assert vacancy.salary_from == 50000
    assert vacancy.salary_to == 70000
    assert vacancy.currency == "RUB"
    assert vacancy.location == "Москва"


def test_empty_name_raises_value_error():
    with pytest.raises(ValueError, match="Название вакансии не должно быть пустым."):
        Vacancy("2", "", "http://example.com/job/2", None, None, "Описание", "RUB", "Локация")


def test_salary_validation():
    vacancy = Vacancy(
        "3",
        "Тестировщик",
        "http://example.com/job/3",
        -100,
        None,
        "Ищем квалифицированного тестировщика.",
        "RUB",
        "Санкт-Петербург",
    )

    assert vacancy.salary_from == 0
    assert vacancy.salary_to == 0


def test_salary_comparisons():
    vacancy1 = Vacancy(
        "4",
        "Младший разработчик",
        "http://example.com/job/4",
        40000,
        50000,
        "Позиция для начинающих.",
        "RUB",
        "Екатеринбург",
    )

    vacancy2 = Vacancy(
        "5",
        "Старший разработчик",
        "http://example.com/job/5",
        80000,
        100000,
        "Позиция для опытных специалистов.",
        "RUB",
        "Екатеринбург",
    )

    assert vacancy1 < vacancy2
    assert vacancy1 <= vacancy2
    assert vacancy2 > vacancy1
    assert vacancy2 >= vacancy1
    assert not (vacancy1 == vacancy2)


def test_cast_to_object_list():
    data = [
        {
            "id": "6",
            "name": "Ведущий разработчик",
            "alternate_url": "http://example.com/job/6",
            "salary": {"from": 90000, "to": 120000, "currency": "RUB"},
            "snippet": {"requirement": "Эксперт в Python."},
            "area": {"name": "Калининград"},
        }
    ]

    vacancies = Vacancy.cast_to_object_list(data)

    assert len(vacancies) == 1
    assert vacancies[0].id == "6"
    assert vacancies[0].name == "Ведущий разработчик"
    assert vacancies[0].salary_from == 90000
    assert vacancies[0].salary_to == 120000
    assert vacancies[0].currency == "RUB"
    assert vacancies[0].location == "Калининград"
