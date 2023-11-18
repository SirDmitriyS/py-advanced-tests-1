import pytest

from main import get_unique_ids, list_to_dict, queries_by_words_distr


class TestUniqueIds:
    @pytest.mark.parametrize(
        'ids,expected', [
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [213, 98, 98, 35]},
            [15, 35, 54, 98, 119, 213]),
            ({'user1': [119, 3, 77, 45, 7]},
            [3, 7, 45, 77, 119]),
            ({'user1': [115, 115, 115, 65, 115],
			'user2': [33, 33, 21, 93, 93],
			'user3': [33]},
            [21, 33, 65, 93, 115]),
        ]
    )
    def test_with_correct_dict(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'ids,expected', [
            ({'user1': [213, 213, 213, 15, 213],
			'user2': [54, 54, 119, 119, 119],
			'user3': [213, 98, 98, 35]},
            [35, 54, 98, 119, 213]),
            ({'user1': [119, 3, 77, 45, 7]},
            [3, 7, 45, 77, 119, 123]),
            ({'user1': [115, 115, 115, 65, 115],
			'user2': [33, 33, 21, 93, 93],
			'user3': [33]},
            [21, 33, 93, 65, 115]),
        ]
    )
    def test_with_wrong_data(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'ids,expected', [
            ([[213, 213, 213, 15, 213],
			[54, 54, 119, 119, 119],
			[213, 98, 98, 35]],
            None),
            ({'user1': [213, [213, [213, 15, 213]]]},
            None),
            ('текст',
            None),
        ]
    )
    def test_with_no_dict(self, ids, expected):
        result = get_unique_ids(ids)
        assert result == expected


class TestQueriesDistr:
    @pytest.mark.parametrize(
        'queries, expected',[
            ([
                'смотреть сериалы онлайн',
                'новости спорта',
                'афиша кино',
                'курс доллара',
                'сериалы этим летом',
                'курс по питону',
                'сериалы про спорт'
            ], [(2, 43), (3, 57)]),
            (['новости науки'], [(2, 100)]),
            ([
                'новости науки', 
                'новости по информационным технологиям'
            ], [(2, 50), (4, 50)])
        ]
    )
    def test_correct_data(self, queries, expected):
        result = queries_by_words_distr(queries)
        assert result == expected

    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'queries, expected',[
            ([
                'смотреть сериалы онлайн',
                'новости спорта',
                'афиша кино',
                'курс доллара',
                'сериалы этим летом',
                'курс по питону',
                'сериалы про спорт'
            ], [(3, 57), (2, 43)]),
            (['новости науки'], [(2, 99)]),
            ([
                'новости науки', 
                'новости по информационным технологиям'
            ], [(2, 50), (3, 50)])
        ]
    )
    def test_wrong_data(self, queries, expected):
        result = queries_by_words_distr(queries)
        assert result == expected

class TestListToDict:
    @pytest.mark.parametrize(
        'input,expected', [
            (['2018-01-01', 'yandex', 'cpc', 100], 
            {'2018-01-01': {'yandex': {'cpc': 100}}}),
            (['2018-01-01', 'yandex', 'cpc'], 
            {'2018-01-01': {'yandex': 'cpc'}}),
            (['2018-01-01', 'yandex'], 
            {'2018-01-01': 'yandex'})
        ]
    )
    def test_correct_data(self, input, expected):
        result = list_to_dict(input)
        assert result == expected
    
    @pytest.mark.xfail
    @pytest.mark.parametrize(
        'input,expected', [
            (['2018-01-01', 'yandex', 'cpc', 100], 
            {'yandex': {'cpc': 100}}),
            (['2018-01-01', 'yandex', 'cpc'], 
            ('2018-01-01', 'yandex','cpc')),
            (['2018-01-01', 'yandex', 'cpc', 100], 
            {100: {'cpc': {'yandex': '2018-01-01'}}}),
        ]
    )
    def test_wrong_data(self, input, expected):
        result = list_to_dict(input)
        assert result == expected
    
    @pytest.mark.xfail
    def test_one_element_list(self):
        assert list_to_dict(['проверка функции'])
        