import sys


def count(args):
    return sum(args[0::2]) - sum(args[1::2])

try:
    print(count(list(map(int, sys.argv[1:]))))
except IndexError:
    print('NO PARAMS')
except Exception as e:
    print(e)
