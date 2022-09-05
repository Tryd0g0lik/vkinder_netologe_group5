import vk_api
import vk
import os

def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def mainAutor(login, password):
    """ Пример обработки двухфакторной аутентификации """
    vk_session = vk_api.VkApi(
        login, password,
        scope = "FRIEND.STORIES.MESSAGES",
    # функция для обработки двухфакторной аутентификации
        auth_handler=auth_handler
    )

    try:
        vk_session.auth()
    except vk_api.AuthError as error_msg:
        print(error_msg)
        return
    return vk_session



def renameFile():
    os.rename("vk_config.v2.json", "vk_config.json")
    return


class apiFunction:
    def __init__(self, token, id):
        """
        :param token: Key for work in vk througth user-profile
        :param id: User id

        """
        self.token = token
        self.id = id

    def getUser(self):
        """
        :return: data-user
        """


        return





