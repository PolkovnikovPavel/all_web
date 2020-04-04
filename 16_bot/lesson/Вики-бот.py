import random
import wikipedia

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.messages.send(user_id=user_id,
                     message=message,
                     random_id=random.randint(0, 2 ** 64))

wikipedia.set_lang('ru')
token = "dae89ed236d52913daf61830694636678d54ac9db4827bc1c9b0b65edab9af1bf0e5ea94b018735b0887d"
# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)   # пример бота из учебника не работал,
for event in longpoll.listen():     # поэтому код немного другой

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk = vk_session.get_api()

            string = '''Привет, вы можете у меня узнать все что угодно
Просто напишите "что такое <ваш запрос>"'''

            if 'что такое ' in event.text.lower():
                try:
                    request = event.text.lower().split('что такое ')[-1]
                    string = wikipedia.summary(request, sentences=3)
                    string += f'\nдля более подробной информации {wikipedia.page(request).url}'
                except:
                    string = 'Увы, но по вашему запросу не удалось ничего найти'

            write_msg(event.user_id, string)
