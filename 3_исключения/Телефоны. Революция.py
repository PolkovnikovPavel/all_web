class num_Exception(Exception):
    pass


codes = [(910, 919), (980, 989), (920, 939), (902, 906), (960, 969)]

operator_codes = []
for code in codes:
    operator_codes.extend(range(code[0], code[1] + 1))

countries_codes = ['+7', '+1', '+55', '+359']


def check_num(num):
    num = ''.join(num.split())

    count = 0
    for s in num:
        if s == '-':
            if num.index(s) == 0 or num.index(s) == len(num) - 1:
                raise num_Exception('неверный формат')
            count += 1
            if count == 2:
                raise num_Exception('неверный формат')
        else:
            count = 0

    count = 0
    for s in num:
        if s == '(':
            count += 1
            if count == 2:
                raise num_Exception('неверный формат')
        if s == ')':
            count -= 1
            if count < 0:
                raise num_Exception('неверный формат')
    if count != 0:
        raise num_Exception('неверный формат')

    bed_symbols = ['-', '(', ')']
    result = ''
    for s in num:
        if s not in bed_symbols:
            result += s

    if not any(map(lambda x: x in result, countries_codes)):
        raise num_Exception('не определяется код страны')

    if result[0] != '+' and result[0] == '8':
        result = '+7' + result[1:]

    if not result[1:].isdigit():
        raise num_Exception('неверный формат')

    if len(result) != 12:
        raise num_Exception('неверное количество цифр')

    if int(result[2:5]) not in operator_codes:
        raise num_Exception('не определяется оператор сотовой связи')

    return result


try:
    print(check_num(input()))
except num_Exception as exc:
    print(exc)


