import vk_api
import datetime


def main():
    login, password = '89505876657', ''
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    all_friends = []
    response = vk.friends.get(fields="bdate, city")
    if response['items']:
        for i in response['items']:
            if 'bdate' in i:
                all_friends.append((i['last_name'], i['first_name'], i['bdate']))
            else:
                all_friends.append((i['last_name'], i['first_name'], 'неизвестно'))
    all_friends.sort(key=lambda x: x[0])
    print('\n'.join(list(map(lambda x: f'{x[0]} {x[1]}, дата рождения: {x[2]}', all_friends))))


if __name__ == '__main__':
    main()
