import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token = "TOKEN"
# Авторизуемся как сообщество
vk_session = vk_api.VkApi(token=token)

longpoll = VkLongPoll(vk_session)   # пример бота из учебника не работал,
for event in longpoll.listen():     # поэтому код немного другой

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk = vk_session.get_api()
            response = vk.users.get(user_id=event.user_id, fields='city')

            strings = [f"Привет, {response[0]['first_name']}\nКак поживает {response[0]['city']['title']}?"]

            vk.messages.send(user_id=event.user_id,
                             message=strings,
                             random_id=random.randint(0, 2 ** 64))
