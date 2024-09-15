import pytest
from src.vacanciec_storage import VacancyStorageJson


@pytest.fixture
def vac_storage(tmp_path):
    """Фикстура для тестирования, что создает новый экземпляр VacancyStorageJson с временным файлом."""
    storage = VacancyStorageJson(file_name=tmp_path / "vacancy_storage.json")
    return storage


@pytest.fixture
def vacancy_data():
    return [
        {
            "id": "107278549",
            "name": "Frontend разработчик (React js)",
            "alternate_url": "http://example.com/1",
            "salary": {"from": 9000000, "to": 0, "currency": "UZS"},
            "snippet": {
                "requirement": "Опыт работы во frontend-разработке от 3-х лет. Хорошие знания CSS3/Sass, HTML5, Bootstrap 5, Tailwind; Typescript."
            },
            "area": {"name": "Ташкент"},
        },
        {
            "id": "106289770",
            "name": "Frontend-разработчик",
            "alternate_url": "http://example.com/2",
            "salary": {"from": 300000, "to": 0, "currency": "RUR"},
            "snippet": {
                "requirement": "Отличные знания JavaScript. Опыт работы с React от 3х лет. Опыт работы с Typescript, Redux."
            },
            "area": {"name": "Москва"},
        },
        {
            "id": "107260582",
            "name": "Frontend Разработчик React TypeScript",
            "alternate_url": "http://example.com/3",
            "salary": {"from": 250000, "to": 0, "currency": "RUR"},
            "snippet": {
                "requirement": "Опыт разработки веб и мобильных приложений на React, опыт в Webapp. Продвинутое владение TypeScript. Понимание и опыт применения современных архитектурных..."
            },
            "area": {"name": "Москва"},
        },
        {
            "id": "106397930",
            "name": "Frontend-разработчик (React, TypeScript)",
            "alternate_url": "http://example.com/4",
            "salary": {"from": 180000, "to": 260000, "currency": "RUR"},
            "snippet": {
                "requirement": "Хорошее знание JavaScript и TypeScript (мы используем TypeScript + JSX). Понимание базовых frontend-технологий..."
            },
            "area": {"name": "Москва"},
        },
        {
            "id": "107246701",
            "name": "Фронтенд разработчик (frontend developer)",
            "alternate_url": "http://example.com/5",
            "salary": {"from": 165000, "to": 190000, "currency": "RUR"},
            "snippet": {"requirement": "Требования: опыт работы с js от 2х лет; опыт работы с vue 2/3, typescript..."},
            "area": {"name": "Санкт-Петербург"},
        },
        {
            "id": "107028340",
            "name": "Frontend-разработчик",
            "alternate_url": "http://example.com/6",
            "salary": {"from": 160000, "to": 0, "currency": "RUR"},
            "snippet": {"requirement": "Опытный специалист, обладающий глубокими знаниями JavaScript/ TypeScript..."},
            "area": {"name": "Санкт-Петербург"},
        },
        {
            "id": "107180789",
            "name": "Middle Frontend developer",
            "alternate_url": "http://example.com/7",
            "salary": {"from": 150000, "to": 250000, "currency": "RUR"},
            "snippet": {"requirement": "Коммерческий опыт Frontend разработки от 2,5 лет..."},
            "area": {"name": "Москва"},
        },
        {
            "id": "107186552",
            "name": "Frontend разработчик (Frontend Developer)",
            "alternate_url": "http://example.com/8",
            "salary": {"from": 150000, "to": 350000, "currency": "RUR"},
            "snippet": {"requirement": "Знание HTML, TypeScript, RxJS, Angular 2+..."},
            "area": {"name": "Москва"},
        },
        {
            "id": "107049849",
            "name": "Frontend-разработчик",
            "alternate_url": "http://example.com/9",
            "salary": {"from": 150000, "to": 0, "currency": "RUR"},
            "snippet": {"requirement": "Высшее образование. Опыт работы программистом от 2 лет..."},
            "area": {"name": "Москва"},
        },
        {
            "id": "107244672",
            "name": "Frontend developer (React)",
            "alternate_url": "http://example.com/10",
            "salary": {"from": 130000, "to": 250000, "currency": "RUR"},
            "snippet": {"requirement": "Хорошие навыки верстки HTML5/CSS3/LESS..."},
            "area": {"name": "Москва"},
        },
    ]
