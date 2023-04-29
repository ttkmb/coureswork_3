import pytest

from utils.load_json_file import load_json
from utils.sort_data import sort_data

data = [
    {'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01', 'operationAmount': 100, 'description': 'test', 'from': 'A',
     'to': 'B'},
    {'id': 2, 'state': 'CANCELED', 'date': '2019-01-02', 'operationAmount': 200, 'description': 'test', 'from': 'B',
     'to': 'C'},
    {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-03', 'operationAmount': 300, 'description': 'test', 'from': 'C',
     'to': 'D'}]


def test_sort_execute():
    assert sort_data(data) == [
        {'id': 3, 'state': 'EXECUTED', 'date': '2022-01-03', 'operationAmount': 300, 'description': 'test', 'from': 'C',
         'to': 'D'},
        {'id': 1, 'state': 'EXECUTED', 'date': '2021-01-01', 'operationAmount': 100,
         'description': 'test', 'from': 'A',
         'to': 'B'},
    ]


def test_sort_empty():
    data_test = []
    assert sort_data(data_test) == []


def test_sort_miss_fields():
    data_test = [{'id': 1, 'state': 'EXECUTED', 'operationAmount': 100, 'description': 'test', 'from': 'A', 'to': 'B'},
                 {'id': 2, 'state': 'PENDING', 'date': '2021-01-02', 'operationAmount': 200, 'description': 'test',
                  'from': 'B', 'to': 'C'},
                 {'id': 3, 'state': 'EXECUTED', 'date': '2021-01-03', 'operationAmount': 300, 'description': 'test'}]
    with pytest.raises(KeyError):
        assert sort_data(data_test) == []


def test_sort_canceled():
    data_test = [
        {'id': 1, 'state': 'CANCELED', 'date': '2021-01-01', 'operationAmount': 100, 'description': 'test', 'from': 'A',
         'to': 'B'},
        {'id': 2, 'state': 'CANCELED', 'date': '2019-01-02', 'operationAmount': 200, 'description': 'test', 'from': 'B',
         'to': 'C'},
        {'id': 3, 'state': 'CANCELED', 'date': '2022-01-03', 'operationAmount': 300, 'description': 'test', 'from': 'C',
         'to': 'D'}]
    assert sort_data(data_test) == []
