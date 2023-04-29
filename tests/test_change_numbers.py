from utils.change_numbers import change_card_numbers


def test_change_numbers():
    assert change_card_numbers('Maestro 1596837868705199') == 'Maestro 1596 83** **** 5199'
    assert change_card_numbers('64686473678894779589') == 'Счет **9589'
