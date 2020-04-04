import random
import datetime

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.messages.send(user_id=user_id,
                     message=message,
                     random_id=random.randint(0, 2 ** 64))


week   = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница',  'суббота', 'воскресенье']
key_words_time = ['врем', 'число', 'дата', 'день', 'врем', 'час']


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

            str = f"{response[0]['first_name']} {response[0]['last_name']} это вы? Я про вас всё знаю!! ахахаха!\n\nВы можете у меня спросить время"
            if event.text.lower() == 'нет':
                str = 'Не ври'
            elif event.text.lower() == 'ладно':
                str = 'Я же говорил НЕ ПИСАТь'
            elif any(map(lambda x: x in event.text.lower(), key_words_time)):
                moscow_time = datetime.datetime.now()
                date = f'{moscow_time.year}-{moscow_time.month}-{moscow_time.day}'
                time = f'{moscow_time.hour}:{moscow_time.minute}:{moscow_time.second}'
                weekday = week[moscow_time.weekday()]

                str = f"дата: {date}\nвремя: {time}\nдень недели: {weekday}"

            write_msg(event.user_id, str)

