import json
import operator


def load_json():
    with open('operations.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def sort_data():
    data = load_json()
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


def print_operation():
    data = sort_data()
    data_of_operation = [(d['date'], d['description'], d['from'], d['to'], d['operationAmount']['amount'], d['operationAmount']['currency']['name']) for d in data]
    data_of_operation_result = []
    for operation in data_of_operation[:5]:
        data_of_operation_result.append(
            f"""\n{operation[0]} {operation[1]}\n{operation[2]} -> {operation[3]}\n{operation[4]} {operation[5]}\n
        """
        )
    return " ".join(data_of_operation_result)






print(print_operation())

# {data['from']} -> {data['to']}


# return f"""{data['date']} {data['description']}\n{data['from']} -> {data['to']}{data['operationAmount']['currency']['name']}\n{data['operationAmount']['amount']}
    # """