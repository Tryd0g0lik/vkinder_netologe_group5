import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_API_VK, VERSION_API_VK


class api:
    def __init__(self):
        self._vk = vk_api.VkApi(token=TOKEN_API_VK)
        self.vk = self._vk.get_api()

    def user(self, user_id):
        res = self.vk.users.get(user_ids=user_id)[0]
        print(f"API =======> user =======> {res}")
        return res

    def search_users(self, filter):
        # city, sex, status, age_from, age_to
        count = 10
        arr_user = {}
        list_users = []
        res1 = self.vk.users.search(
            city=filter[0], sex=filter[1],
            status=filter[2], age_from=filter[3],
            age_to=filter[4], has_photo=True, count=count)
        for user in res1['items']:
            if user['is_closed'] is not True:
                res = self.vk.photos.get(
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
                l = []
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
        return arr_user
