import random
import datetime
import wikipedia

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    print(random.randint(0, 2 ** 64))
    vk.messages.send(user_id=user_id,
                     message=message,
                     random_id=random.randint(0, 2 ** 64))


week   = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница',  'суббота', 'воскресенье']
key_words_time = ['врем', 'число', 'дата', 'день', 'врем', 'час']
key_words_help = ['что ты можешь?', 'help', 'что ты можешь', '/help',
                  'на что ты способен', 'все возможности', 'помоги']


wikipedia.set_lang('ru')
# API-ключ созданный ранее
token = "dae89ed236d52913daf61830694636678d54ac9db4827bc1c9b0b65edab9af1bf0e5ea94b018735b0887d"

# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

# Работа с сообщениями
longpoll = VkLongPoll(vk_session)

print("Server started")
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk = vk_session.get_api()
            response = vk.users.get(user_id=event.user_id)

            print(event)
            print('Новое сообщение:')
            print('Для меня от:', response)
            print('Текст:', event.text)

            str = f'Я не понимаю вас, а чтоб понимал воспользуйтесь командами. Чтоб узнать команды напиши "что ты можешь?" или "help"'
            if event.text.lower() == 'нет':
                str = 'Не ври'
            elif event.text.lower() == '':
                str = 'Крутой стикер!'
            elif event.text.lower() == 'ладно':
                str = 'Я же говорил НЕ ПИСАТь'
            elif event.text.lower() == 'как дела' or event.text.lower() == 'чё как':
                str = 'Круто, мне массаж делают, чтоб я мог больше, а у тебя?'
            elif event.text.lower() == 'привет' or event.text.lower() == 'хай':
                str = 'Привет привет'
            elif any(map(lambda x: event.text.lower() == x, key_words_help)):
                str = '''Я могу:
> Подскозать москавское время (просто спроси)
> Найти информацию на вики (напиши "Что такое <ваш запрос>")
> Написать ваше сообщение админу (напиши "Скажи админу <ваше сообщение>")
> Остальное появится позже!'''

            elif any(map(lambda x: x in event.text.lower(), key_words_time)):
                moscow_time = datetime.datetime.now()
                date = f'{moscow_time.year}-{moscow_time.month}-{moscow_time.day}'
                time = f'{moscow_time.hour}:{moscow_time.minute}:{moscow_time.second}'
                weekday = week[moscow_time.weekday()]

                str = f"дата: {date}\nвремя: {time}\nдень недели: {weekday}"
            elif 'что такое ' in event.text.lower():
                try:
                    request = event.text.lower().split('что такое ')[-1]
                    str = wikipedia.summary(request, sentences=3)
                    str += f'\nДля более подробной информации {wikipedia.page(request).url}'
                except:
                    str = 'Увы, но по вашему запросу не удалось ничего найти'
            elif 'скажи админу ' in event.text.lower():
                str = 'Сообщение успешно отправлено!'
                try:
                    request = event.text.lower().split('скажи админу ')[-1]
                    string = '___________________\n'
                    string += f'| сообщение от {response[0]["first_name"]} {response[0]["last_name"]}\n|\n'

                    string += request + '\n|\n| конец\n___________________'
                    write_msg(449876815, string)
                except:
                    str = 'Ошибка в отправке'



            write_msg(event.user_id, str)

