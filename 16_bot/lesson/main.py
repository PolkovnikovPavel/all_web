import vk_api
import datetime


def main():
    login, password = LOGIN, PASSWORD
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()

    response = vk.wall.get(count=5, offset=1)
    if response['items']:
        for i in response['items']:
            time = datetime.datetime.fromtimestamp(i['date'])
            print('{', i['text'], '}', sep='')
            print(time.strftime('date: {%Y-%m-%d}, time: {%H:%M:%S}'))


if __name__ == '__main__':
    main()
