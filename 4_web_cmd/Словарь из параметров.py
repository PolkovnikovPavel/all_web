import sys


def dictionaries(args):
    dictionary = {}
    sort = False
    if '--sort' in ' '.join(args):
        sort = True

    for arg in args:
        if '--' not in arg:
            key, value = arg.split('=')
            dictionary[key] = value
    result = []

    keys = list(dictionary.keys())
    if sort:
        keys.sort()

    for key in keys:
        result.append(f'Key: {key} Value: {dictionary[key]}')
    return '\n'.join(result)


print(dictionaries(sys.argv[1:]))
