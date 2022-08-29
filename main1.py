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
    print(event)
    if event.type == VkBotEventType.MESSAGE_NEW:
        if event.object.message['text'] == 'Кнопка':
            #print(f"------------------------------------>{event.object.message['from_id']}")
            keyboard = VkKeyboard(one_time=False)
            keyboard.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY, payload={"type":"coll"})
            vk.messages.send(
                peer_id=event.object.message['from_id'],
                random_id=get_random_id(),
                keyboard=keyboard.get_keyboard(),
                message='Пример клавиатуры'
            )

    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print(event)
        print(f'----------------------------->TYT')
        b = VkKeyboard()
        vk.messages.send(
            peer_id=event.object.user_id,
            random_id=get_random_id(),
            keyboard=b.get_empty_keyboard(),
            message='Пример удаления клавиатуры'
        )
        keyboard = VkKeyboard(one_time=False)
        keyboard.add_callback_button(label='Добавить СИНИЙ', color=VkKeyboardColor.PRIMARY,
                                     payload={"type": "coll"})
        vk.messages.send(
            peer_id=event.object.user_id,
            random_id=get_random_id(),
            keyboard=keyboard.get_keyboard(),
            message='Синяяя кнопка'
        )