import random
import datetime

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.messages.send(user_id=user_id,
                     message=message,
                     random_id=random.randint(0, 2 ** 64))


week   = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница',  'суббота', 'воскресенье']
token = "TOKEN"
# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)   # пример бота из учебника не работал,
for event in longpoll.listen():     # поэтому код немного другой

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk = vk_session.get_api()

            string = '''Привет, вы можете у меня узнать день недели по дате в формате "YYYY-MM-DD"'''

            text = event.text
            try:
                text = text.split('-')
                if len(text[0]) != 4:
                    raise Exception
                if len(text[1]) != 2:
                    raise Exception
                if len(text[2]) != 2:
                    raise Exception
                year, month, day = map(int, text)
                date = datetime.date(year, month, day)
                string = f'На {"-".join(text)} день недели: {week[date.weekday()]}'
            except:
                pass

            write_msg(event.user_id, string)
