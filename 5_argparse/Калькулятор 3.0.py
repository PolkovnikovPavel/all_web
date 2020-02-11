import argparse


def copy_file(start_file, end_file, upper, lines):
    with open(start_file, 'r') as f:
        start_text = f.read()

    if lines > len(start_text.split('\n')):
        lines = len(start_text.split('\n'))
    if lines == -1:
        lines = len(start_text.split('\n'))
    text = '\n'.join(start_text.split('\n')[:lines])

    if upper:
        text = text.upper()

    with open(end_file, 'w') as fi:
        fi.write(text)
        fi.close()


parser = argparse.ArgumentParser()
parser.add_argument('numbers', nargs='*')

args = parser.parse_args()

numbers = args.numbers

try:
    if len(numbers) == 1:
        print('TOO FEW PARAMS')
    elif len(numbers) == 0:
        print('NO PARAMS')
    elif len(numbers) > 2:
        print('TOO MUCH PARAMS')
    else:
        print(int(numbers[0]) + int(numbers[1]))
except Exception as e:
    print(e.__class__.__name__)
