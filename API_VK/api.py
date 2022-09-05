import vk_api
from config import DSN, TOKEN_API_VK


class api:
    favorites = []
    blacklist = []
    def __init__(self):
        self._vk = vk_api.VkApi(token=TOKEN_API_VK)
        self.vk = self._vk.get_api()
        self.offset = 0

    def user(self, user_id):
        res = self.vk.users.get(user_ids=user_id)[0]
        self.user_id=user_id
        return res

    def open_user(self, offset, filters, command='search'):
        count = 1
        self.offset = offset
        self.command = command

        res = self.vk.users.search(
            city=filters[0], sex=filters[1],
            status=filters[2], age_from=filters[3],
            age_to=filters[4], has_photo=True, count=count, offset=self.offset)

        if self.command == 'search':
            if res['items'][0]['is_closed'] is not False:
                offset += 1
        elif self.command == 'search_back':
            if res['items'][0]['is_closed'] is not False:
                offset -= 1
                if offset < 0:
                    command = 'search'
                    offset = 0
        elif self.command == 'search_next':
            if len(res['items'][0]) > 0:
                if res['items'][0]['is_closed'] is not False:
                    offset += 1
            else:
                offset -=1
        if res['items'][0]['is_closed'] is not True:
            res['offset'] = offset
            return res
        else:
            if offset < 0:
                self.command = 'search'
                offset = 0
            return self.open_user(offset, filters, command)

    def search_users(self, offset, filters, command):
        # city, sex, status, age_from, age_to
        self.command = command
        self.filters = filters
        self.offset = offset
        arr_user = {}
        list_users = []
        user = self.open_user(offset, filters, command)
        res = self.vk.photos.get(
            owner_id=user['items'][0]['id'],
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
            l.append(f"photo{user['items'][0]['id']}_{photo}")

        arr_user1 = {}
        arr_user1['id_user'] = user['items'][0]['id']
        arr_user1['first_name'] = user['items'][0]['first_name']
        arr_user1['last_name'] = user['items'][0]['last_name']
        arr_user1['photo'] = l
        list_users.append(arr_user1)

        arr_user['offset'] = user['offset']
        arr_user['count'] = user['count']
        arr_user['users'] = list_users
        return arr_user

    def insert_favorites(self, id_user):
        if id_user not in self.blacklist:
            self.favorites.append(id_user)
        return self.favorites

    def insert_blacklist(self, id_user):
        if id_user not in self.favorites:
            self.blacklist.append(id_user)
        return self.blacklist

    def update_filter(self, new_filter):
        self.filter = list(map(int, new_filter.split(',')))
        return self.filter

    def view_favorites(self, user_id):
        #из БД выбрать
        result = self.favorites
        return result

    def view_blacklist(self, user_id):
        #Из БД выбрать
        result = self. blacklist
        return result
