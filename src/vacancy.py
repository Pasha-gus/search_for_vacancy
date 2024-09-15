class Vacancy:
    __slots__ = ("id", "name", "url", "salary_from", "salary_to", "description", "currency", "location")

    def __init__(
        self,
        id: str,
        name: str,
        url: str,
        salary_from: float,
        salary_to: float,
        description: str,
        currency: str,
        location: str,
    ):
        self.id = id
        self.name = self._validate_name(name)
        self.url = url
        self.salary_from = self._validate_salary(salary_from)
        self.salary_to = self._validate_salary(salary_to)
        self.description = description
        self.currency = currency
        self.location = location

    def _validate_name(self, name: str) -> str:
        if not name:
            raise ValueError("Название вакансии не должно быть пустым.")
        return name

    def _validate_salary(self, salary: float) -> float:
        return salary if salary is not None and salary >= 0 else 0

    def __repr__(self):
        return (
            f"Vacancy(id='{self.id}', name='{self.name}', salary_from={self.salary_from}, "
            f"salary_to={self.salary_to}, currency='{self.currency}', location='{self.location}', "
            f"description='{self.description}')"
        )

    def __lt__(self, other):
        return self.salary_from < other.salary_from

    def __le__(self, other):
        return self.salary_from <= other.salary_from

    def __eq__(self, other):
        return self.salary_from == other.salary_from

    def __ne__(self, other):
        return self.salary_from != other.salary_from

    def __gt__(self, other):
        return self.salary_from > other.salary_from

    def __ge__(self, other):
        return self.salary_from >= other.salary_from

    @staticmethod
    def cast_to_object_list(data: list[dict]) -> list["Vacancy"]:
        vacancies = []
        for items in data:
            id = items.get("id")
            name = items.get("name")
            url = items.get("alternate_url")

            salary_info = items.get("salary")
            salary_from = salary_info.get("from") if salary_info else None
            salary_to = salary_info.get("to") if salary_info else None

            description = items.get("snippet", {}).get("requirement", "")
            currency = salary_info.get("currency", "") if salary_info else ""
            location = items.get("area", {}).get("name", "")

            vacancy = Vacancy(id, name, url, salary_from, salary_to, description, currency, location)
            vacancies.append(vacancy)
        return vacancies
