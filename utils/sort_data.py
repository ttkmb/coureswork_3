import operator
from utils.load_json_file import load_json

data = load_json()


def sort_data(data):
    '''
    Сортирую полученный файл по полю 'date', проверяя пустые словари
    '''
    dict_to_use = []
    executed_dict = []
    for operation in data:
        if 'date' and 'from' in operation and operation['state'] == 'EXECUTED':
            dict_to_use.append(operation)
    sorted_data = sorted(dict_to_use, key=operator.itemgetter('date'), reverse=True)
    for d in sorted_data:
        executed = {'id': d['id'], 'state': d['state'], 'date': d['date'], 'operationAmount': d['operationAmount'],
                    'description': d['description'], 'from': d['from'], 'to': d['to']}
        executed_dict.append(executed)
    return executed_dict

