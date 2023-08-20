import json
from abc import ABC, abstractmethod


class FileSaver(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def get_vacancies_by_salary(self, salary):
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy):
        pass


class JSONSaver(FileSaver):

    def add_vacancy(self, vacancy):
        with open('list_of_vacancies.json', 'w') as file:
            json.dump(vacancy, file)
        return None

    def get_vacancies_by_salary(self, salary):
        pass

    def delete_vacancy(self, vacancy):
        pass
