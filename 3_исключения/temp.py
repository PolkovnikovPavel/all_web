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
    for s in num[1:]:
        if s not in bed_symbols:
            result += s
    return '+7' + result


print(check_num(input()))
