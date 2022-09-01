import json
from Bot.Bot import Bot
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK, GROUP_ID


vk_session = vk_api.VkApi(token=TOKEN_BOT)

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

command = {'start', 'help', 'next', 'back', 'search', 'filter', 'favorites', 'blacklist'}




for event in longpoll.listen():
    #print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.object.message['text'].lower() in command:
            if event.object.message['text'].lower() == 'start':
                keyboard = VkKeyboard(one_time=False)
                keyboard.add_callback_button(label='🔍 ПОИСК', color=VkKeyboardColor.SECONDARY, payload={"type": "search"})
                keyboard.add_line()
                keyboard.add_callback_button(label='⭐ Избранные', color=VkKeyboardColor.POSITIVE, payload={"type": "favorites"})
                keyboard.add_callback_button(label='✘ Чёрный список', color=VkKeyboardColor.NEGATIVE, payload={"type": "blacklist"})
                keyboard.add_line()
                keyboard.add_callback_button(label='⚙ Фильтр', color=VkKeyboardColor.SECONDARY, payload={"type": "filter"})
                keyboard.add_callback_button(label='🚑 HELP', color=VkKeyboardColor.PRIMARY, payload={"type": "help"})

                vk.messages.send(
                    peer_id=event.object.message['from_id'],
                    random_id=get_random_id(),
                    keyboard=keyboard.get_keyboard(),
                    message='Привет, бродяга! Для продолжения работы используй кнопки действия!'
                )

            elif event.object.message['text'].lower() == 'help':
                vk.messages.send(
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
                vk.messages.send(
                    peer_id=event.object.message['from_id'],
                    random_id=get_random_id(),
                    keyboard=keyboard_sender.get_keyboard(),
                    message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
                )

            elif event.object.message['text'].lower() == 'filter':
                vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести фильтры для изменения!!!!!"
                )
            elif event.object.message['text'].lower() == 'favorites':
                vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести всех избранных пользователей!!!!!"
                )
            elif event.object.message['text'].lower() == 'blacklist':
                vk.messages.send(
                    user_id=event.object.user_id,
                    random_id=get_random_id(),
                    message="Вывести всех пользователей из черного списка!!!!!"
                )

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print(event)
        print(f"{event.object.conversation_message_id}================={event.object.peer_id}")
        if event.object.payload['type'] == 'help':
            vk.messages.send(
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
        elif event.object.payload['type'] == 'search':
            keyboard_sender = VkKeyboard(inline=True)
            keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY, payload={"type": "back"})
            keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
                                                payload={"type": "add_in_blacklist"})
            keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
                                                payload={"type": "add_in_favorites"})
            keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY, payload={"type": "next"})
            vk.messages.send(
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
            vk.messages.send(
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
            #В массиве необходимо перебрать все наши фильтры из таблицы фильтры
            vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Введите через запятую в фильтр формата [Возраст от,Возраст до,Город,Пол,Семейное положение]"
            )
        elif event.object.payload['type'] == 'favorites':
            vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Вывести всех ИЗБРАННЫХ пользователей!!!!!"
            )

        elif event.object.payload['type'] == 'blacklist':
            vk.messages.send(
                user_id=event.object.user_id,
                random_id=get_random_id(),
                message="Вывести всех пользователей из черного списка!!!!!"
            )