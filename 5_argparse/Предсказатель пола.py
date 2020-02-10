import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--barbie", default=50, type=int)
parser.add_argument("--cars", default=50, type=int)
parser.add_argument("--movie", choices=['melodrama', 'other',
                                        'football'], default='other')

args = parser.parse_args()

barbie = args.barbie
if barbie < 0 or barbie > 100:
    barbie = 50

cars = args.cars
if cars < 0 or cars > 100:
    cars = 50

if args.movie == 'melodrama ':
    movie = 0
elif args.movie == 'other':
    movie = 50
else:
    movie = 100

boy = int((100 - barbie + cars + movie) / 3)
girl = 100 - boy

print(f'boy: {boy}')
print(f'girl: {girl}')
