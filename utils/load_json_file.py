import json


def load_json():
    '''
    Загрузка json файла, не понял как правильно узазать путь(../ не работал) решил остановиться на полном пути.
    '''
    with open('/Users/ttkmb/WORKHARD/coureswork_3/operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

