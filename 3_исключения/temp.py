class num_Exception(Exception):
    pass


def check_num(num):
    num = ''.join(num.split())
    if num[0] != '8' and num[:2] != '+7':
        raise num_Exception('не верное начало номера')

    count = 0
    for s in num:
        if s == '-':
            if num.index(s) == 0 or num.index(s) == len(num) - 1:
                raise num_Exception('символ "-" не может быть в начале и в конце')
            count += 1
            if count == 2:
                raise num_Exception('символ "-" не может быть двойным')
        else:
            count = 0

    count = 0
    for s in num:
        if s == '(':
            count += 1
            if count == 2:
                raise num_Exception('допустима только одна пара скобок')
        if s == ')':
            count -= 1
            if count < 0:
                raise num_Exception('не верное использование скобок')
    if count != 0:
        raise num_Exception('не верное использование скобок')

    bed_symbols = ['-', '(', ')']
    result = ''
    for s in num:
        if s not in bed_symbols:
            result += s
    if result[0] != '+':
        result = '+7' + result[1:]

    if len(result) != 12:
        raise num_Exception('не верная длина номера')

    return result


try:
    print(check_num(input()))
except num_Exception as exc:
    print('error')
#except Exception as exc:
#    print(f'не известная ошибка: {exc}')

