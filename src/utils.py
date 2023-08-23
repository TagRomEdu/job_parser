from src.file_saver import JSONSaver


def sort_vac(vacancies_lst, word_lst):
    """
    Sorting by salary, if salary of vac >= salary of func
    """

    sorted_vac_lst = []
    for vacancy in vacancies_lst:
        if isinstance(vacancy["requirements"], dict):
            for word in word_lst:
                if word in vacancy["requirements"]["requirement"].replace(',', '').split(" "):
                    sorted_vac_lst.append(vacancy)
        else:
            for word in word_lst:
                if word in vacancy["requirements"].replace(',', '').split(" "):
                    sorted_vac_lst.append(vacancy)
    return sorted_vac_lst


def job_selection(vacancy_lst):
    """
    Sorting by keywords and adding sorting by salary
    """
    json_f_1 = JSONSaver()

    for i in range(len(vacancy_lst)):
        json_f_1.add_vacancy(vacancy_lst[i])

    salary = int(input("Укажите желаемую стартовую зарплату: "))
    vac_list = json_f_1.get_vacancies_by_salary(salary)

    filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split(' ')
    sorted_vacancies = sort_vac(vac_list, filter_words)

    if not sorted_vacancies:
        print("Таких вакансий нет!")

    for vacancy in sorted_vacancies:
        print(
            f'{vacancy["name"]} - {vacancy["salary"]} {vacancy["currency"]} - {vacancy["url"]} - {vacancy["location"]}')
