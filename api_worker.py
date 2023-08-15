from abc import ABC, abstractmethod
import os


class APIWorker(ABC):
    API_SJ = os.getenv('API_SuperJob')
    HH_VACANCIES = 'https://api.hh.ru/vacancies'

    @abstractmethod
    def get_object(self):
        """
        method gets object works with API
        """
        pass

    @abstractmethod
    def get_vacations(self):
        """
        method gets list of vacations
        """
        pass


class APIHeadHunter(APIWorker):
    def __init__(self):
        pass

    def get_object(self):
        pass

    def get_vacations(self):
        pass
