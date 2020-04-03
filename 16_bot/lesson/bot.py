import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message,
                                'random_id': random.randint(0, 2048)})


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
            print(event)
            print('Новое сообщение:')

            vk = vk_session.get_api()
            response = vk.users.get(user_id=event.user_id)
            print('Для меня от:', response)

            print('Текст:', event.text)
            str = f"Павел Полковников крутой, а {response[0]['first_name']} {response[0]['last_name']} лох какой-то"
            vk.messages.send(user_id=event.user_id,
                             message=str,
                             random_id=random.randint(0, 2 ** 64))
