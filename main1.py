import json
from Bot.Bot import Bot
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK, GROUP_ID
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from API_VK.api import api

vk_session = vk_api.VkApi(token=TOKEN_BOT)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

command = {'start', 'help', 'next', 'back', 'search', 'filter', 'favorites', 'blacklist'}
message_id = 0

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print(f"MESSAGE_NEW ========>  {event}")
        if event.object.message['text'].lower() in command:
            if event.object.message['text'].lower() == 'start':
                user = api().user(event.object.message['from_id'])

                keyboard = VkKeyboard(one_time=False)
                keyboard.add_callback_button(label='🔍 ПОИСК', color=VkKeyboardColor.SECONDARY,
                                             payload={"type": "search"})
                keyboard.add_line()
                keyboard.add_callback_button(label='⭐ Избранные', color=VkKeyboardColor.POSITIVE,
                                             payload={"type": "favorites"})
                keyboard.add_callback_button(label='✘ Чёрный список', color=VkKeyboardColor.NEGATIVE,
                                             payload={"type": "blacklist"})
                keyboard.add_line()
                keyboard.add_callback_button(label='⚙ Фильтр', color=VkKeyboardColor.SECONDARY,
                                             payload={"type": "filter"})
                keyboard.add_callback_button(label='🚑 HELP', color=VkKeyboardColor.PRIMARY, payload={"type": "help"})

                message_id = vk.messages.send(
                    peer_id=event.object.message['peer_id'],
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message=f'Привет, {user["first_name"]}! Для продолжения работы используй кнопки действия!'
                )
            elif event.object.message['text'].lower() == 'help':
                message_id = vk.messages.send(
                    peer_id=event.object.message['from_id'],
                    random_id=get_random_id(),
                    message="Справка по командам:\n"
                            "help - справка\n"
                            "start - начать работу с ботом\n"
                            "search - поиск пользователей по заданному фильтру\n"
                            "filter - настройка фильтра поиска\n"
                            "favorites - список избранных пользователей\n"
                            "blacklist - список пользователей попавших в черный список"
                )
            elif event.object.message['text'].lower() == 'search':

                keyboard_sender = VkKeyboard(inline=True)
                keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY,
                                                    payload={"type": "back"})
                keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
                                                    payload={"type": "add_in_blacklist"})
                keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
                                                    payload={"type": "add_in_favorites"})
                keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY,
                                                    payload={"type": "next"})
                # Имя
                # Фамилия
                # ссылка
                # на
                # профиль

                # 3 фото attachment(https: // dev.vk.com / method / messages.send)
                # filter = {'city': 99, 'sex': 1, 'status': 6, 'age_from': 20, 'age_to': 20}
                filter = (99, 2, 6, 20, 23)
                users = api().search_users(filter)
                for item in users['users']:
                    print(item)
                    vk.messages.send(
                        peer_id=event.object.message['from_id'],
                        random_id=get_random_id(),
                        message=f'{item["first_name"]} {item["last_name"]}\n'
                                f'<a href="https://vk.com/id{item["id_user"]}">LINK</a>',
                        attachment=item['photo']
                    )

                message_id = vk.messages.send(
                    peer_id=event.object.message['from_id'],
                    random_id=get_random_id(),
                    keyboard=keyboard_sender.get_keyboard(),
                    message=f'По вашему запросу найдено {users["count"]} человек\n'
                )
            elif event.object.message['text'].lower() == 'filter':
                message_id = vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести фильтры для изменения!!!!!"
                )
            elif event.object.message['text'].lower() == 'favorites':
                message_id = vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести всех избранных пользователей!!!!!"
                )
            elif event.object.message['text'].lower() == 'blacklist':
                message_id = vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести всех пользователей из черного списка!!!!!"
                )

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print(event)
        print(f"{event.object.conversation_message_id}================={event.object.peer_id}")

        print(f"MESSAGE_ID = {message_id}")
        if message_id is not None and message_id != 0:
            vk.messages.delete(
                message_ids=message_id,
                delete_for_all=True,
                peer_id=event.object.user_id
            )
            print(f"DROP   Message_id = {event.object.id}")

        if event.object.payload['type'] == 'help':
            message_id = vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Справка по командам:\n"
                        "help - справка\n"
                        "start - начать работу с ботом\n"
                        "search - поиск пользователей по заданному фильтру\n"
                        "filter - настройка фильтра поиска\n"
                        "favorites - список избранных пользователей\n"
                        "blacklist - список пользователей попавших в черный список"
            )
            print(f"MESS ========> {message_id}")
        elif event.object.payload['type'] == 'search':
            keyboard_sender = VkKeyboard(inline=True)
            keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
            keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "add_in_blacklist"})
            keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
                                                payload={"type": "add_in_favorites"})
            keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
            message_id = vk.messages.send(
                peer_id=event.object.user_id,
                random_id=get_random_id(),
                keyboard=keyboard_sender.get_keyboard(),
                message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
            )

        elif event.object.payload['type'] == 'next':
            print('NEXT')
            keyboard_sender = VkKeyboard(inline=True)
            keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
            keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "add_in_blacklist"})
            keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
                                                payload={"type": "add_in_favorites"})
            keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
            message_id = vk.messages.send(
                peer_id=event.object.user_id,
                random_id=get_random_id(),
                keyboard=keyboard_sender.get_keyboard(),
                message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
            )

            # keyboard_sender = VkKeyboard(inline=True)
            # keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
            # keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
            #                                     payload={"type": "add_in_blacklist"})
            # keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
            #                                     payload={"type": "add_in_favorites"})
            # keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
            #
            # vk.messages.edit(
            #     peer_id=event.object.peer_id,
            #     conversation_message_id=event.object.conversation_message_id,
            #     keyboard=keyboard_sender.get_keyboard(),
            #     message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
            # )
        elif event.object.payload['type'] == 'back':
            print('BACK')
        elif event.object.payload['type'] == 'add_in_favorites':
            print('add_in_favorites')
        elif event.object.payload['type'] == 'add_in_blacklist':
            print('add_in_blacklist')

        elif event.object.payload['type'] == 'filter':
            # В массиве необходимо перебрать все наши фильтры из таблицы фильтры
            message_id = vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Введите через запятую в фильтр формата [Возраст от,Возраст до,Город,Пол,Семейное положение]"
            )
        elif event.object.payload['type'] == 'favorites':
            message_id = vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Вывести всех ИЗБРАННЫХ пользователей!!!!!"
            )

        elif event.object.payload['type'] == 'blacklist':
            message_id = vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Вывести всех пользователей из черного списка!!!!!"
            )
