import json
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK, GROUP_ID
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from API_VK.api import api
from Bot.vkBot import vkBot

vk_session = vk_api.VkApi(token=TOKEN_BOT)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

command = {'start', 'help', 'search_next', 'search_back', 'search', 'filter_setting', 'filter', 'add_favorites', 'add_blacklist', 'favorites', 'blacklist'}

id_user = 0
offset = 0
count_users = 0
message_id = 0
filter = (99, 2, 6, 20, 20)
event_command = ''

bot = vkBot()
for event in longpoll.listen():
    random_id = get_random_id()
    if event.type == VkBotEventType.MESSAGE_NEW:
        peer_id = event.object.message['peer_id']
        event_command = event.object.message['text'].lower()

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        peer_id = event.object.peer_id
        event_command = event.object.payload['type']

        # print(f"{event.object.conversation_message_id}================={event.object.peer_id}")
        #
        # print(f"MESSAGE_ID = {message_id}")
        # if message_id is not None and message_id != 0:
        #     vk.messages.delete(
        #         message_ids=message_id,
        #         delete_for_all=True,
        #         peer_id=event.object.user_id
        #     )
        #     print(f"DROP   Message_id = {event.object.id}")

        # if event.object.payload['type'] == 'help':
        #     message_id = vk.messages.send(
        #         user_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         message="Справка по командам:\n"
        #                 "help - справка\n"
        #                 "start - начать работу с ботом\n"
        #                 "search - поиск пользователей по заданному фильтру\n"
        #                 "filter - настройка фильтра поиска\n"
        #                 "favorites - список избранных пользователей\n"
        #                 "blacklist - список пользователей попавших в черный список"
        #     )
        #     print(f"MESS ========> {message_id}")
        # elif event.object.payload['type'] == 'search':
        #     keyboard_sender = VkKeyboard(inline=True)
        #     keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
        #     keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
        #                                         payload={"type": "add_in_blacklist"})
        #     keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
        #                                         payload={"type": "add_in_favorites"})
        #     keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
        #     message_id = vk.messages.send(
        #         # peer_id=event.object.user_id,
        #         user_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         keyboard=keyboard_sender.get_keyboard(),
        #         message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
        #     )
        #
        # elif event.object.payload['type'] == 'next':
        #     print('NEXT')
        #     keyboard_sender = VkKeyboard(inline=True)
        #     keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
        #     keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
        #                                         payload={"type": "add_in_blacklist"})
        #     keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
        #                                         payload={"type": "add_in_favorites"})
        #     keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
        #     message_id = vk.messages.send(
        #         peer_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         keyboard=keyboard_sender.get_keyboard(),
        #         message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
        #     )
        #
        #     # keyboard_sender = VkKeyboard(inline=True)
        #     # keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
        #     # keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
        #     #                                     payload={"type": "add_in_blacklist"})
        #     # keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
        #     #                                     payload={"type": "add_in_favorites"})
        #     # keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
        #     #
        #     # vk.messages.edit(
        #     #     peer_id=event.object.peer_id,
        #     #     conversation_message_id=event.object.conversation_message_id,
        #     #     keyboard=keyboard_sender.get_keyboard(),
        #     #     message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
        #     # )
        # elif event.object.payload['type'] == 'back':
        #     print('BACK')
        # elif event.object.payload['type'] == 'add_in_favorites':
        #     print('add_in_favorites')
        # elif event.object.payload['type'] == 'add_in_blacklist':
        #     print('add_in_blacklist')
        #
        # elif event.object.payload['type'] == 'filter':
        #     # В массиве необходимо перебрать все наши фильтры из таблицы фильтры
        #     message_id = vk.messages.send(
        #         user_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         message="Введите через запятую в фильтр формата [Возраст от,Возраст до,Город,Пол,Семейное положение]"
        #     )
        # elif event.object.payload['type'] == 'favorites':
        #     message_id = vk.messages.send(
        #         user_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         message="Вывести всех ИЗБРАННЫХ пользователей!!!!!"
        #     )
        #
        # elif event.object.payload['type'] == 'blacklist':
        #     message_id = vk.messages.send(
        #         user_id=event.object.user_id,
        #         random_id=get_random_id(),
        #         message="Вывести всех пользователей из черного списка!!!!!"
        #     )





    print("===============================================================")
    if event_command == 'start':
        user = api().user(event.object.message['from_id'])
        keyboard = bot.menu_keyboard()
        message = f'Привет, {user["first_name"]}! Для продолжения работы используй кнопки действия!'
        message_id = bot.message(peer_id, random_id, message, keyboard)
        print(f"Start====>  {message_id}")
    elif event_command == 'help':
        message = bot.bot_help_message()
        message_id = bot.message(peer_id, random_id, message)
        print(f"HELP====>   {message_id}")

    elif 'search' in event_command:
        if event_command == 'search':
            offset = 0
            command = 'search'
        elif event_command == 'search_next':
            if offset > count_users:
                offset = count_users
            else:
                offset += 1
            command = 'search_next'
        elif event_command == 'search_back':
            if offset > 0:
                offset -= 1
                command = 'search_back'
            else:
                offset = 0
                command = 'search'
        users = api().search_users(offset, filter, command)
        offset = users['offset']
        count_users = users["count"]
        keyboard = bot.menu_search()
        message = f'{users["users"][0]["first_name"]} {users["users"][0]["last_name"]}\n' \
                  f'https://vk.com/id{users["users"][0]["id_user"]}'
        attachment = users['users'][0]['photo']
        message_id = bot.message(peer_id, random_id, message, keyboard, attachment)
        id_user = users["users"][0]["id_user"]
        print(f"SEARCH={command}===> {message_id}")

    elif event_command == 'add_favorites':
        if id_user != 0:
            list_favorites = api().insert_favorites(id_user)
            message = f"Пользователь добавлен в избранные!!!!! В вашем листе {list_favorites}"
            message_id = bot.message(peer_id, random_id, message)
            print(f"ADD_FAVORITES====>{message_id}")

    elif event_command == 'add_blacklist':
        if id_user != 0:
            list_black = api().insert_blacklist(id_user)
            message = f"Пользователь добавлен в чёрный список!!!!! В вашем листе {list_black}"
            message_id = bot.message(peer_id, random_id, message)
            print(f"ADD_BLACKLIST====>{message_id}")

    elif event_command == 'filter':
        message = f"Тип фильтра (Город, Пол, Семейное положение, Возраст с, Возраст по). В данный момент фильтр {filter}"
        message_id = bot.message(peer_id, random_id, message)
        print(f"FILTER====>{message_id}")

    elif 'filter_setting' in event_command:
        string = event.object.message['text'].lower().replace("filter_setting", "")
        new_filter = api().update_filter(string)
        filter = new_filter
        message = f"Фильтры изменён на {new_filter}!!!!!"
        message_id = bot.message(peer_id, random_id, message)
        print(f"FILTER_SETTING====>{message_id}")

    elif event_command == 'favorites':
        message = ''
        list_favorite = api().view_favorites(event.object.message['from_id'])
        for item in list_favorite:
            message += f"{item}\n"
        message = f"Ваши избранные пользователи {len(list_favorite)}:\n{message}"
        message_id = bot.message(peer_id, random_id, message)
        print(f"FAVORITES====>{message_id}")

    elif event_command == 'blacklist':
        message = ''
        list_blacklist = api().view_blacklist(event.object.message['from_id'])
        for item in list_blacklist:
            message += f"{item}\n"
        message = f"Ваши пользователи из чёрного списка {len(list_blacklist)}:\n{message}"
        message_id = bot.message(peer_id, random_id, message)
        print(f"BLACKLIST====>{message_id}")







    # if event.object.message['text'].lower() == 'start':
    #     user = api().user(event.object.message['from_id'])
    #     keyboard = bot.menu_keyboard()
    #     message = f'Привет, {user["first_name"]}! Для продолжения работы используй кнопки действия!'
    #     message_id = bot.message(peer_id, random_id, message, keyboard)
    #     print(f"Start====>  {message_id}")
    # elif event.object.message['text'].lower() == 'help':
    #     message = bot.bot_help_message()
    #     message_id = bot.message(peer_id, random_id, message)
    #     print(f"HELP====>   {message_id}")
    #
    # elif 'search' in event.object.message['text'].lower():
    #     if event.object.message['text'].lower() == 'search':
    #         offset = 0
    #         command = 'search'
    #     elif event.object.message['text'].lower() == 'search_next':
    #         if offset > count_users:
    #             offset = count_users
    #         else:
    #             offset += 1
    #         command = 'search_next'
    #     elif event.object.message['text'].lower() == 'search_back':
    #         if offset > 0:
    #             offset -= 1
    #             command = 'search_back'
    #         else:
    #             offset = 0
    #             command = 'search'
    #     users = api().search_users(offset, filter, command)
    #     offset = users['offset']
    #     count_users = users["count"]
    #     keyboard = bot.menu_search()
    #     message = f'{users["users"][0]["first_name"]} {users["users"][0]["last_name"]}\n' \
    #               f'https://vk.com/id{users["users"][0]["id_user"]}'
    #     attachment = users['users'][0]['photo']
    #     message_id = bot.message(peer_id, random_id, message, keyboard, attachment)
    #     id_user = users["users"][0]["id_user"]
    #     print(f"SEARCH={command}===> {message_id}")
    #
    # elif event.object.message['text'].lower() == 'add_favorites':
    #     if id_user != 0:
    #         list_favorites = api().insert_favorites(id_user)
    #         message = f"Пользователь добавлен в избранные!!!!! В вашем листе {list_favorites}"
    #         message_id = bot.message(peer_id, random_id, message)
    #         print(f"ADD_FAVORITES====>{message_id}")
    #
    # elif event.object.message['text'].lower() == 'add_blacklist':
    #     if id_user != 0:
    #         list_black = api().insert_blacklist(id_user)
    #         message = f"Пользователь добавлен в чёрный список!!!!! В вашем листе {list_black}"
    #         message_id = bot.message(peer_id, random_id, message)
    #         print(f"ADD_BLACKLIST====>{message_id}")
    #
    # elif event.object.message['text'].lower() == 'filter':
    #     message = f"Тип фильтра (Город, Пол, Семейное положение, Возраст с, Возраст по). В данный момент фильтр {filter}"
    #     message_id = bot.message(peer_id, random_id, message)
    #     print(f"FILTER====>{message_id}")
    #
    # elif 'filter_setting' in event.object.message['text'].lower():
    #     string = event.object.message['text'].lower().replace("filter_setting", "")
    #     new_filter = api().update_filter(string)
    #     filter = new_filter
    #     message = f"Фильтры изменён на {new_filter}!!!!!"
    #     message_id = bot.message(peer_id, random_id, message)
    #     print(f"FILTER_SETTING====>{message_id}")
    #
    # elif event.object.message['text'].lower() == 'favorites':
    #     message = ''
    #     list_favorite = api().view_favorites(event.object.message['from_id'])
    #     for item in list_favorite:
    #         message += f"{item}\n"
    #     message = f"Ваши избранные пользователи {len(list_favorite)}:\n{message}"
    #     message_id = bot.message(peer_id, random_id, message)
    #     print(f"FAVORITES====>{message_id}")
    #
    # elif event.object.message['text'].lower() == 'blacklist':
    #     message = ''
    #     list_blacklist = api().view_blacklist(event.object.message['from_id'])
    #     for item in list_blacklist:
    #         message += f"{item}\n"
    #     message = f"Ваши пользователи из чёрного списка {len(list_blacklist)}:\n{message}"
    #     message_id = bot.message(peer_id, random_id, message)
    #     print(f"BLACKLIST====>{message_id}")

