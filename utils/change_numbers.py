def change_card_numbers(number_card):
    '''
    Меняю номер карт или счета на звездочки
    '''
    number_digit = number_card.split(' ')[-1]
    if len(number_digit) == 20:
        return f'Счет **{number_digit[16:]}'
    else:
        if 'Visa' in number_card:
            card_type_visa = ' '.join(number_card.split(' ')[:2])
            return f'{card_type_visa} {number_digit[0:4]} {number_digit[4:6]} ** **** {number_digit[12:]}'
        else:
            card_type_other = ' '.join(number_card.split(' ')[:1])
            return f'{card_type_other} {number_digit[0:4]} {number_digit[4:6]} ** **** {number_digit[12:]}'