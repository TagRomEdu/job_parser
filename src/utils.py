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
