import argparse


parser = argparse.ArgumentParser()
parser.add_argument('values', nargs='*')
parser.add_argument("--sort", action='store_true')


args = parser.parse_args()

sort = args.sort
values = list(map(lambda x: x.split('='), args.values))
if sort:
    values.sort(key=lambda x: x[0])
data = {}
for value in values:
    data[value[0]] = value[1]

for key in data:
    print(f'Key: {key}\tValue: {data[key]}')
