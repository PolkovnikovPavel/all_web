import vk_api
import os
import datetime
def main():
    login, password = '89505876657', 'setorg652431'
    vk_session = vk_api.VkApi(login, password)
    try:
        vk_session.auth(token_only=True)
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    vk = vk_session.get_api()


    upload = vk_api.VkUpload(vk_session)
    photo = upload.photo_wall(['static/img/paris_2.jpeg']
                              )

    vk_photo_id = f"photo{photo[0]['owner_id']}_{photo[0]['id']}"

    print(photo, vk_photo_id, sep="\n")
    vk = vk_session.get_api()
    #vk.wall.post(message="Test", attachments=[vk_photo_id])




    #upload = vk_api.VkUpload(vk_session)
    #upload.photo('photo449876815_457240393', '271455451', group_id='193732812')

if __name__ == '__main__':
    main()
