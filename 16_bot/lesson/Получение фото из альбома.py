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
    # Используем метод wall.get

    response = vk.photos.get(album_id='271455451', group_id='193732812')
    for item in response['items']:
        size = item['sizes'][-1]
        print(f'url: {size["url"]} size: {size["width"]}x{size["height"]}')



if __name__ == '__main__':
    main()
