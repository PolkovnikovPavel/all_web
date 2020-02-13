import argparse

COUNT = {'year': 360, 'week': 7, 'month': 30, 'day': 1}


def convert_from_day_to(num, type):
    return num * COUNT[type]


def calculat_per(day, week, month, year, type_result):
    per_week = week / COUNT['week']
    per_month = month / COUNT['month']
    per_year = year / COUNT['year']

    all_per = day + per_week + per_month + per_year
    return convert_from_day_to(all_per, type_result)


parser = argparse.ArgumentParser()
parser.add_argument("--per-day", default=0, type=int)
parser.add_argument("--per-week", default=0, type=int)
parser.add_argument("--per-month", default=0, type=int)
parser.add_argument("--per-year", default=0, type=int)
parser.add_argument("--get-by", choices=['day', 'month', 'year'],
                    default='day')

args = parser.parse_args()
per_day = args.per_day
per_week = args.per_week
per_month = args.per_month
per_year = args.per_year
get_by = args.get_by

print(int(calculat_per(per_day, per_week, per_month, per_year, get_by)))
