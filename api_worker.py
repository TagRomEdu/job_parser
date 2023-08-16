from abc import ABC, abstractmethod
import os
import json
import requests


class APIWorker(ABC):
    API_SJ = os.getenv('API_SuperJob')
    HH_VACANCIES = 'https://api.hh.ru/vacancies'
    SJ_VACANCIES = 'https://api.superjob.ru/2.0/vacancies'

    headers_sj = {'X-Api-App-Id': API_SJ}

    @abstractmethod
    def get_vacancies(self):
        """
        method returns list of vacancies
        """
        pass


class HeadHunterAPI(APIWorker):
    def __init__(self, name):
        self.name = name

    def get_vacancies(self) -> dict:
        request = requests.get(self.HH_VACANCIES)
        return request.json()


class SuperJobAPI(APIWorker):
    def __init__(self, name):
        self.name = name

    def get_vacancies(self) -> dict:
        request = requests.get(self.SJ_VACANCIES, headers=self.headers_sj)
        return request.json()

