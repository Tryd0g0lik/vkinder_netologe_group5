import os
import vk_api
import json

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def main(login, password):
    """ Пример обработки двухфакторной аутентификации """


    vk_session = vk_api.VkApi(
        login, password,
        # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return

    # ...

def renameFile():
    os.rename("vk_config.v2.json", "vk_config.json")
    return


if __name__ == '__main__':
    if not os.path.exists("vk_config.json"):
        if not os.path.exists("vk_config.v2.json"):
            login, passw = input("Login: "), input("Passw: ")
            main(login, passw)
            vk_login = vk_api.VkApi(login, passw)
            vk_login.token['access_token']

        if not os.path.exists("vk_config.json"):
            renameFile()
    else:
        if not os.path.exists("vk_config.json"):
            renameFile()

    with open("vk_config.json", "r") as vkv2:
        dict_var = json.load(vkv2)
        token = dict_var[login]["token"]["app6222115"]["scope_140492255"]\
            ["access_token"]
        id_user = dict_var[login]["token"]["app6222115"]["scope_140492255"]\
                  ["user_id"]


