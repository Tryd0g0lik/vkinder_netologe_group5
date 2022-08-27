import requests
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK
import vk_api
from vk_api import longpoll, bot_longpoll, keyboard


if __name__ == '__main__':
    vk_session = vk_api.VkApi(token=TOKEN_API_VK)
    vk = vk_session.get_api()

    print(vk.users.search(q='Сергей Рогачевский', city=99))