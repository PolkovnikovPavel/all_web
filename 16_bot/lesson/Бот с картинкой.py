import random

import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


token = "TOKEN"
login, password = LOGIN, PASSWORD

# Авторизуемся как сообщество и человек
vk_session_group = vk_api.VkApi(token=token)
vk_session = vk_api.VkApi(login, password)
try:
    vk_session.auth(token_only=True)
except vk_api.AuthError as error_msg:
    print(error_msg)
vk_group = vk_session_group.get_api()
vk = vk_session.get_api()

response = vk.photos.get(album_id='271455451', group_id='193732812')
images = []
for item in response['items']:
    images.append((item['owner_id'], item['id']))


longpoll = VkLongPoll(vk_session_group)
for event in longpoll.listen():

    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            vk_group = vk_session_group.get_api()
            user = vk_group.users.get(user_id=event.user_id, fields='city')

            img = random.choice(images)
            attachment = f'photo{img[0]}_{img[1]}'

            strings = [f"Добро пожаловать {user[0]['first_name']} {user[0]['last_name']}"]

            vk_group.messages.send(user_id=event.user_id,
                             message=strings,
                             random_id=random.randint(0, 2 ** 64),
                             attachment=attachment)
