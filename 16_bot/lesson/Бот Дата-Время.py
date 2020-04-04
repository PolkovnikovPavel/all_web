import random
import datetime

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType

week   = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница',  'суббота', 'воскресенье']
key_words = ['время', 'число', 'дата', 'день']
token = "TOKEN"
# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)   # пример бота из учебника не работал,
for event in longpoll.listen():     # поэтому код немного другой

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk = vk_session.get_api()

            strings = f"Привет, вы можете у меня спросить время"

            if any(map(lambda x: x in event.text, key_words)):
                moscow_time = datetime.datetime.now(
                    datetime.timezone(datetime.timedelta(hours=3)))
                date = f'{moscow_time.year}-{moscow_time.month}-{moscow_time.day}'
                time = f'{moscow_time.hour}:{moscow_time.minute}:{moscow_time.second}'
                weekday = week[moscow_time.weekday()]

                strings = f"дата: {date}\nвремя: {time}\nдень недели: {weekday}"


            vk.messages.send(user_id=event.user_id,
                             message=strings,
                             random_id=random.randint(0, 2 ** 64))
