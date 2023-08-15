from abc import ABC, abstractmethod


class APIWorker(ABC):

    @abstractmethod
    def get_object(self):
        pass

    @abstractmethod
    def get_vacations(self):
        pass
