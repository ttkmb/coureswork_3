from utils.sort_data import sort_data
from utils.change_numbers import change_card_numbers
from utils.load_json_file import load_json

json_file = load_json()
sorted_data = sort_data(json_file)


def print_operation():
    '''
    Вывод последних 5 отсортированных операций и применения на них реформации номеров на звездочки
    '''
    data_of_operation = [(d['date'], d['description'], d['from'], d['to'], d['operationAmount']['amount'],
                          d['operationAmount']['currency']['name']) for d in sorted_data]
    data_of_operation_result = []
    for operation in data_of_operation[:5]:
        date = operation[0].find("T")
        sliced_date = operation[0][:date]
        parts = sliced_date.split('-')
        reversed_parts = parts[::-1]
        joined_date = "-".join(reversed_parts)
        number_from = change_card_numbers(operation[2])
        number_to = change_card_numbers(operation[3])
        data_of_operation_result.append(
            f"""\n{joined_date} {operation[1]}\n{number_from} -> {number_to}\n{operation[4]} {operation[5]}
        """
        )
    print(" ".join(data_of_operation_result))


print_operation()
