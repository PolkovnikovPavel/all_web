import vk_api
import os
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

    upload = vk_api.VkUpload(vk_session)

    upload.photo('photo449876815_457240392', '271455451', '193732812')


if __name__ == '__main__':
    main()
