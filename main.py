# Задание 2
# Выведите на экран все уникальные гео-ID из значений словаря ids.
# Т.е. список вида [213, 15, 54, 119, 98, 35]
def get_unique_ids(ids):
    unique_ids = {user_id for user_ids in list(
        ids.values()) for user_id in user_ids}
    result = list(unique_ids)
    result.sort()
    return result


# Задание 3
# Дан список поисковых запросов. Получить распределение количества слов в них.
# Т.е. поисковых запросов из одного - слова 5%, из двух - 7%, из трех - 3% и т.д.
def queries_by_words_distr(queries):
    queries_len = [query.count(' ') + 1 for query in queries]
    queries_len_distr = {len_val: queries_len.count(
        len_val) for len_val in set(queries_len)}
    queries_count = sum(queries_len_distr.values())
    queries_distr = [(query_len, round(queries_len_distr[query_len] /
                      queries_count * 100)) for query_len in queries_len_distr]
    queries_distr.sort(key=lambda x: x[0])
    return queries_distr


# Задание 5
# Напишите код для преобразования произвольного списка вида ```['2018-01-01', 'yandex', 'cpc', 100]``` (он может быть любой длины)
# в словарь ```{'2018-01-01': {'yandex': {'cpc': 100}}}```
def list_to_dict(input_list):
    if len(input_list) < 2:
        raise BaseException('Для создания словаря из списка в нем должно быть минимум 2 элемента')

    dict_from_list = {input_list[-2]: input_list[-1]}
    for list_item in reversed(input_list[:-2]):
        dict_from_list = {list_item: dict_from_list}

    return dict_from_list


if __name__ == '__main__':
    ids = {'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [213, 98, 98, 35]}
    print(get_unique_ids(ids))

    queries = [
        'смотреть сериалы онлайн',
        'новости спорта',
        'афиша кино',
        'курс доллара',
        'сериалы этим летом',
        'курс по питону',
        'сериалы про спорт'
    ]
    print(queries_by_words_distr(queries))

    input_list = ['2018-01-01', 'yandex', 'cpc', 100]
    print(list_to_dict(input_list))
