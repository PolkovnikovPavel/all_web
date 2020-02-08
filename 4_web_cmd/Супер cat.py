import sys


def parsing(commands):
    global file_name, num, count, sort
    sort = False
    num = False
    count = False

    if '--sort' in commands:
        sort = True
    if '--num' in commands:
        num = True
    if '--count' in commands:
        count = True
    for command in commands:
        if '--' not in command:
            file_name = command


parsing(sys.argv[1:])

try:
    with open(file_name) as file:
        text = file.read()
    if sort:
        strings = text.split('\n')
        strings.sort()
        text = '\n'.join(strings)

    if num:
        strings = text.split('\n')
        text = []
        for i in range(len(strings)):
            text.append(f'{i} {strings[i]}')
        text = '\n'.join(text)

    if count:
        count = len(text.split('\n'))
        text += f'\nrows count: {count}'

    print(text)

except Exception:
    print('ERROR')
