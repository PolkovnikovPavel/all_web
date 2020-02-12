import argparse


def get_text(file_name, sort, num, count):
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

        return text

    except Exception:
        return 'ERROR'


parser = argparse.ArgumentParser()
parser.add_argument('file_name')
parser.add_argument("--count", action='store_true')
parser.add_argument("--num", action='store_true')
parser.add_argument("--sort", action='store_true')

args = parser.parse_args()

file_name = args.file_name
count = args.count
num = args.num
sort = args.sort

print(get_text(file_name, sort, num, count))

