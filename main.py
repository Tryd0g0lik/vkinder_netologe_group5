import json

import sqlalchemy
import requests
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll

from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK
import vk_api
from vk_api import longpoll, bot_longpoll, keyboard
from vk_api.longpoll import VkLongPoll, VkEventType

from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id

if __name__ == '__main__':
    # res = requests.get('https://oauth.vk.com/authorize?client_id=51411238&scope=65536&response_type=token').json()
    # print(res)

    _vk = vk_api.VkApi(token=TOKEN_API_VK)
    vk100 = _vk.get_api()
    s = vk100.users.search(q='Сергей Рогачевский', city=99)
    print(s)
    for item, v in s.items():
        print(f"{item}      {v}")
        if item == 'items':
            for ii in v:
                print(ii)
                print(ii['id'])
    print('===============================')
    print(s['items'][0]['first_name'])

    print('----------------------------------------------------------------------------------')

    count = 10
    filter = (99, 1, 6, 20, 23)
    arr_user = {}
    list_users = []
    res1 = vk100.users.search(
        city=filter[0], sex=filter[1],
        status=filter[2], age_from=filter[3],
        age_to=filter[4], has_photo=True, count=count)
    print(f"RES    ======>    {res1}")
    print('----------------------------------------------------------------------------------')

    for user in res1['items']:
        if user['is_closed'] is not True:
            res = vk100.photos.get(
                owner_id=user['id'],
                album_id='profile',
                extended=True,
                photo_sizes=True
            )

            arr_photo = {}
            for photo in res['items']:
                if len(arr_photo) < 3:
                    arr_photo[photo['id']] = photo['likes']['count']
                else:
                    for item, val in arr_photo.items():
                        if photo['likes']['count'] > val:
                            del arr_photo[item]
                            arr_photo[photo['id']] = photo['likes']['count']
                            break
            l=[]
            for photo in arr_photo.keys():
                l.append(f"photo{user['id']}_{photo}")

            arr_user1 = {}
            arr_user1['id_user'] = user['id']
            arr_user1['first_name'] = user['first_name']
            arr_user1['last_name'] = user['last_name']
            arr_user1['photo'] = l
            list_users.append(arr_user1)

        arr_user['count'] = res1['count']
        arr_user['users'] = list_users

    print(arr_user)