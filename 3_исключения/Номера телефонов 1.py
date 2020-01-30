def check_num(num):
    num = ''.join(num.split())
    if num[0] != '8' and num[:2] != '+7':
        return 'error'

    count = 0
    for s in num:
        if s == '-':
            count += 1
            if count == 2:
                return 'error'
        else:
            count = 0

    count = 0
    for s in num:
        if s == '(':
            count += 1
            if count == 2:
                return 'error'
        if s == ')':
            count -= 1
            if count < 0:
                return 'error'

    bed_symbols = ['-', '(', ')']
    result = ''
    for s in num:
        if s not in bed_symbols:
            result += s
    if result[0] != '+':
        result = '+7' + result[1:]

    return result


print(check_num(input()))
