import datetime
import schedule

start_day = datetime.datetime.today().day
last_hour = datetime.datetime.today().hour


def job():
    global last_hour
    if last_hour != datetime.datetime.today().hour:
        print('Ку')
        last_hour = datetime.datetime.today().hour


schedule.every(1).seconds.do(job)


while datetime.datetime.today().day == start_day:
    schedule.run_pending()

