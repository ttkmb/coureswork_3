import json


def load_json():
    '''
    Загружает файл из json
    '''
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

