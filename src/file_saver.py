import json
from abc import ABC, abstractmethod


class FileSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        """
        Method adds info about vacancy to file
        """
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        """
        Method returns list of vacancies sorted by salary
        """

    @abstractmethod
    def delete_vacancy(self, vacancy):
        """
        Method deletes vacancy
        """
        pass


class JSONSaver(FileSaver):

    def add_vacancy(self, vacancy):
        vacancy_lst = []
        vacancy_dict = {"name": vacancy.name, "salary": vacancy.salary, "url": vacancy.url,
                       "requirements": vacancy.requirements, "location": vacancy.location, "currency": vacancy.list}

        try:
            with open('list_of_vacancies.json', 'r', encoding='utf-8') as file:
                contents = json.load(file)
                if vacancy_dict in contents:
                    return None
                else:
                    contents.append(vacancy_dict)
                    with open('list_of_vacancies.json', 'w', encoding='utf-8') as f:
                        json.dump(contents, f, ensure_ascii=False, indent=4)
                        return None

        except FileNotFoundError:
            vacancy_lst.append(vacancy_dict)
            with open('list_of_vacancies.json', 'w', encoding='utf-8') as file:
                json.dump(vacancy_lst, file, ensure_ascii=False, indent=4)
            return None

    def get_vacancies_by_salary(self, salary):
        with open('list_of_vacancies.json', encoding='utf-8') as file:
            data = json.load(file)
        chosen_by_salary = [vac_dict for vac_dict in data
                            if isinstance(vac_dict["salary"], int) and vac_dict["salary"] >= salary]
        return chosen_by_salary

    def delete_vacancy(self, vacancy):
        with open('list_of_vacancies.json', encoding='utf-8') as file:
            data = json.load(file)

        for i, vac in enumerate(data):
            if vac["name"] == vacancy:
                del data[i]

        with open('list_of_vacancies.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
            return None
