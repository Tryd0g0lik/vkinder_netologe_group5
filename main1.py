import json

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK

vk_session = vk_api.VkApi(token=TOKEN_BOT)

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

longpoll = VkBotLongPoll(vk_session, 215581501)
vk = vk_session.get_api()

command = {'start', 'help', 'next', 'back', 'search', 'filter', 'favorites', 'blacklist'}

for event in longpoll.listen():
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        # if event.object.message['text'] == 'start':
        #     #print(f"------------------------------------>{event.object.message['from_id']}")
        #     keyboard = VkKeyboard(one_time=False)
        #     keyboard.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY, payload={"type":"coll"})
        #     vk.messages.send(
        #         peer_id=event.object.message['from_id'],
        #         random_id=get_random_id(),
        #         keyboard=keyboard.get_keyboard(),
        #         message='Пример клавиатуры'
        #     )
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
                ...
            elif event.object.message['text'].lower() == 'next':
                ...
            elif event.object.message['text'].lower() == 'back':
                ...
            elif event.object.message['text'].lower() == 'search':
                # keyboard_sender = VkKeyboard(inline=True)
                # keyboard_sender.add_callback_button(label='⬅   НАЗАД', color=VkKeyboardColor.NEGATIVE,
                #                                     payload={"type": "back"})
                # keyboard_sender.add_callback_button(label='ВПЕРЁД   ➡', color=VkKeyboardColor.POSITIVE,
                #                                     payload={"type": "next"})
                # vk.messages.send(
                #     peer_id=event.object.message['from_id'],
                #     random_id=get_random_id(),
                #     keyboard=keyboard_sender.get_keyboard(),
                #     message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
                # )
                ...
            elif event.object.message['text'].lower() == 'filter':
                ...
            elif event.object.message['text'].lower() == 'favorites':
                ...
            elif event.object.message['text'].lower() == 'blacklist':
                ...

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print(event)
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
            keyboard_sender.add_callback_button(label='⬅   НАЗАД', color=VkKeyboardColor.NEGATIVE, payload={"type": "back"})
            keyboard_sender.add_callback_button(label='ВПЕРЁД   ➡', color=VkKeyboardColor.POSITIVE, payload={"type": "next"})
            vk.messages.send(
                peer_id=event.object.user_id,
                random_id=get_random_id(),
                keyboard=keyboard_sender.get_keyboard(),
                message='Вывести Пользователей на основании сохраненного фильтра!!!!!'
            )

        elif event.object.payload['type'] == 'filter':
            ...
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
        # else:
        #     print(event)
        #     print(f'----------------------------->TYT')
        #     # clear_menu = VkKeyboard()
        #     # vk.messages.send(
        #     #     peer_id=event.object.user_id,
        #     #     random_id=get_random_id(),
        #     #     keyboard=clear_menu.get_empty_keyboard(),
        #     #     message='1111'
        #     # )
        #     print("<---------TYT------------>")
        #     print(event)
        #     print(event.object.payload)
        #     print(event.object.event_id)
        #     vk.messages.sendMessageEventAnswer(
        #         event_id=event.object.event_id,
        #         user_id=event.object.user_id,
        #         peer_id=event.object.peer_id,
        #         event_data=json.dumps(event.object.payload)
        #     )
        # # keyboard = VkKeyboard(one_time=False)
        # # keyboard.add_callback_button(label='Добавить СИНИЙ', color=VkKeyboardColor.PRIMARY,
        # #                              payload={"type": "coll"})
        # # vk.messages.send(
        # #     peer_id=event.object.user_id,
        # #     random_id=get_random_id(),
        # #     keyboard=keyboard.get_keyboard(),
        # #     message='Синяяя кнопка'
        # # )