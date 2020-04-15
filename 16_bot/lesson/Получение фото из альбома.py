import vk_api


def main():
    login, password = '89505876657', ''
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()
    response = vk.photos.get(album_id='твой id альбома', group_id='твой id группы')
    for item in response['items']:
        size = item['sizes'][-1]
        print(f'url: {size["url"]} size: {size["width"]}x{size["height"]}')



if __name__ == '__main__':
    main()
