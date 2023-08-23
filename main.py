from src.api_worker import HeadHunterAPI, SuperJobAPI
from src.vacancies import Vacancy
from src.utils import job_selection


def user_interaction():

    '''json_f_1 = JSONSaver()'''
    platforms = ["1 - HeadHunter", "2 - SuperJob"]

    choice = int(input(f"Выбери платформы, с которых хочешь получить вакансии: {', '.join(platforms)}\n"))

    if choice == 1:
        hh_api = HeadHunterAPI()
        vacancy_lst1 = []
        search_query = input("Выберите язык программирования для фильтра профессий: ")
        py_vac = hh_api.get_vacancies(search_query.lower())

        for i in range(len(py_vac)):
            vacancy_lst1.append(Vacancy(py_vac['items'][i]['name'], py_vac['items'][i]['salary'], py_vac['items'][i]['url'],
                                        py_vac['items'][i]['snippet'], py_vac['items'][i]['area']['name']))
        job_selection(vacancy_lst1)

    if choice == 2:
        sj_api = SuperJobAPI()
        vacancy_lst2 = []
        search_query = input("Выберите язык программирования для фильтра профессий: ")
        py_vac2 = sj_api.get_vacancies(search_query.lower())

        for i in range(len(py_vac2)):
            vacancy_lst2.append(Vacancy(py_vac2['objects'][i]['profession'], py_vac2['objects'][i]['payment_from'],
                                        py_vac2['objects'][i]['link'], py_vac2['objects'][i]['candidat'],
                                        py_vac2['objects'][i]['town']['title'], py_vac2['objects'][i]['currency']))
        job_selection(vacancy_lst2)


if __name__ == "__main__":
    user_interaction()
