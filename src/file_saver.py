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
        vacancy_dict = {"name": vacancy.name, "salary": vacancy.salary, "url": vacancy.url,
                        "requirements": vacancy.requirements, "location": vacancy.location}
        try:
            with open('list_of_vacancies.json', 'r', encoding='utf-8') as file:
                contents = file.read()
                if vacancy_dict["name"] in contents:
                    return None

        except FileNotFoundError:
            with open('list_of_vacancies.json', 'a', encoding='utf-8') as file:
                json.dump(vacancy_dict, file, ensure_ascii=False)
                file.write('\n')
            return None
        else:
            with open('list_of_vacancies.json', 'a', encoding='utf-8') as file:
                json.dump(vacancy_dict, file, ensure_ascii=False)
                file.write('\n')

    def get_vacancies_by_salary(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass
