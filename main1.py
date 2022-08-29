import json

import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK

vk_session = vk_api.VkApi(token=TOKEN_BOT)

from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

longpoll = VkBotLongPoll(vk_session, 215581501)
vk = vk_session.get_api()
from vk_api.longpoll import VkLongPoll, VkEventType

keyboard_1 = VkKeyboard(one_time=False, inline=True)
keyboard_1.add_callback_button(
    label="Кнопка",
    color=VkKeyboardColor.SECONDARY,
    payload={"type": "show_snackbar", "text": "Это исчезающее сообщение на экране"}
)
menu = {
    "one_time": False,
    "buttons": [

        [
            {
                "action": {
                    "type": "callback",
                    "payload": {'find'},
                    "label": "ПОИСК"
                },
                "color": "primary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": {"button": "2"},
                    "label": "Избранные"
                },
                "color": "positive"
            },
            # < span style = 'color:red' >❤ < / span >
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"1\"}",
                    "label": "Черный список"
                },
                "color": "negative"
            }
            # < span style = 'color:black' >✘ < / span >
        ],
        [
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "HELP"
                },
                "color": "secondary"
            },
            {
                "action": {
                    "type": "text",
                    "payload": "{\"button\": \"2\"}",
                    "label": "Настройка поиска"
                },
                "color": "secondary"
            }
        ]
    ]}
command = {'start', 'help', 'next', 'back', 'search', 'filter', 'favorites', 'blacklist'}


def send_menu(id):
    keyboard = VkKeyboard(one_time=True, inline=False)
    keyboard.keyboard = menu
    vk.messages.send(
        peer_id=id,
        random_id=get_random_id(),
        keyboard=keyboard.get_keyboard(),
        message='Привет, бродяга! Для продолжения работы используй кнопки действия!'
    )

for event in longpoll.listen():
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
            if event.object.message['text'] == 'start':
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

            elif event.object.message['text'] == 'help':
                ...
            elif event.object.message['text'] == 'next':
                ...
            elif event.object.message['text'] == 'back':
                ...
            elif event.object.message['text'] == 'search':
                ...
            elif event.object.message['text'] == 'filter':
                ...
            elif event.object.message['text'] == 'favorites':
                ...
            elif event.object.message['text'] == 'blacklist':
                ...
            elif event.object.message['text'] == 'setting_filter':
                ...
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        if event.object.payload['type'] == 'help':
            print(event)
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
        else:
            print(event)
            print(f'----------------------------->TYT')
            # clear_menu = VkKeyboard()
            # vk.messages.send(
            #     peer_id=event.object.user_id,
            #     random_id=get_random_id(),
            #     keyboard=clear_menu.get_empty_keyboard(),
            #     message='1111'
            # )
            print("<---------TYT------------>")
            print(event)
            print(event.object.payload)
            print(event.object.event_id)
            vk.messages.sendMessageEventAnswer(
                event_id=event.object.event_id,
                user_id=event.object.user_id,
                peer_id=event.object.peer_id,
                event_data=json.dumps(event.object.payload)
            )
        # keyboard = VkKeyboard(one_time=False)
        # keyboard.add_callback_button(label='Добавить СИНИЙ', color=VkKeyboardColor.PRIMARY,
        #                              payload={"type": "coll"})
        # vk.messages.send(
        #     peer_id=event.object.user_id,
        #     random_id=get_random_id(),
        #     keyboard=keyboard.get_keyboard(),
        #     message='Синяяя кнопка'
        # )