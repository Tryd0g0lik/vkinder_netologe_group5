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
    print(vk100.users.search(q='Сергей Рогачевский', city=99))

    vk_session = vk_api.VkApi(token=TOKEN_BOT)
    longpool = VkLongPoll(vk_session)
    vk = vk_session.get_api()

    menu = {
        "one_time": False,
        "buttons": [

                [
                    {
                        "action": {
                            "type": "callback",
                            "payload": {'type': 'my_own_100500_type_edit'},
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


    def send_some_msg(id, some_text):
        vk_session.method("messages.send", {"user_id": id, "message": some_text, "random_id": 0})

    for event in longpool.listen():
        print(event.__dict__)
        print(event.__class__)
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                msg = event.text.lower()
                id = event.user_id
                msg_id = event.peer_id

                if msg == "start":
                    #send_some_msg(id, "")
                    send_menu(id)
                    #vk_session.method("messages.send", {"user_id": id, "attachment": 'photo5527523_412507362,photo5527523_412507362' ,"random_id": 0})
                    #vk_session.method("messages.send",{"user_id": id, "attachment": 'photo{id}_{number_photo}}', "random_id": 0})
                    # keyboard = VkKeyboard(one_time=False)
                    # keyboard.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY,
                    #                                payload={"type": "my_own_100500_type_edit"})
                    # vk.messages.send(
                    #     peer_id=id,
                    #     random_id=get_random_id(),
                    #     keyboard=keyboard.get_keyboard(),
                    #     message='Пример клавиатуры'
                    # )




                if msg == "red":
                    ...

    # CALLBACK_TYPES = ('show_snackbar', 'open_link', 'open_app')
    # f_toggle: bool = False
    # APP_ID = 51411238  # id IFrame приложения
    # OWNER_ID = 5527523  # id владельца приложения
    # settings = dict(one_time=False, inline=True)
    # # №1. Клавиатура с 3 кнопками: "показать всплывающее сообщение", "открыть URL" и изменить меню (свой собственный тип)
    # keyboard_1 = VkKeyboard(**settings)
    # # pop-up кнопка
    # keyboard_1.add_callback_button(label='Покажи pop-up сообщение', color=VkKeyboardColor.SECONDARY,
    #                                payload={"type": "show_snackbar", "text": "Это исчезающее сообщение"})
    # keyboard_1.add_line()
    # # кнопка с URL
    # keyboard_1.add_callback_button(label='Откртыть Url', color=VkKeyboardColor.POSITIVE,
    #                                payload={"type": "open_link", "link": "https://vk.com/dev/bots_docs_5"})
    # keyboard_1.add_line()
    # # кнопка по открытию ВК-приложения
    # keyboard_1.add_callback_button(label='Открыть приложение', color=VkKeyboardColor.NEGATIVE,
    #                                payload={"type": "open_app", "app_id": APP_ID, "owner_id": OWNER_ID,
    #                                         "hash": "anything_data_100500"})
    # keyboard_1.add_line()
    # # кнопка переключения на 2ое меню
    # keyboard_1.add_callback_button(label='Добавить красного ', color=VkKeyboardColor.PRIMARY,
    #                                payload={"type": "my_own_100500_type_edit"})
    #
    # # №2. Клавиатура с одной красной callback-кнопкой. Нажатие изменяет меню на предыдущее.
    # keyboard_2 = VkKeyboard(**settings)
    # # кнопка переключения назад, на 1ое меню.
    # keyboard_2.add_callback_button('Назад', color=VkKeyboardColor.NEGATIVE, payload={"type": "my_own_100500_type_edit"})
    #
    #
    #
    # vk_session = vk_api.VkApi(token=TOKEN_BOT, api_version=VERSION_API_VK)
    # vk = vk_session.get_api()
    # longpoll = VkBotLongPoll(vk_session, group_id=215581501)
    # for event in longpoll.listen():
    #     # отправляем меню 1го вида на любое текстовое сообщение от пользователя
    #     if event.type == VkBotEventType.MESSAGE_NEW:
    #         keyboard_1 = VkKeyboard(one_time=False)
    #         print(event.obj.client_info)
    #         if event.obj.message['text'] != '':
    #             if event.from_user:
    #                 # Если клиент пользователя не поддерживает callback-кнопки,
    #                 # нажатие на них будет отправлять текстовые
    #                 # сообщения. Т.е. они будут работать как обычные inline кнопки.
    #                 if 'callback' not in event.obj.client_info['button_actions']:
    #                     print(f'Клиент {event.obj.message["from_id"]} не поддерж. callback')
    #
    #                 vk.messages.send(
    #                                     peer_id=event.obj.message['from_id'],
    #                                     random_id=get_random_id(),
    #                                     keyboard=keyboard_1.get_keyboard(),
    #                                     message='Пример клавиатуры'
    #                                 )
    #                 # vk.messages.send(
    #                 #     user_id=event.obj.message['from_id'],
    #                 #     random_id=get_random_id(),
    #                 #     peer_id=event.obj.message['from_id'],
    #                 #     keyboard=keyboard_1.get_keyboard(),
    #                 #     message=event.obj.message['text'])
    #     # обрабатываем клики по callback кнопкам
    #     elif event.type == VkBotEventType.MESSAGE_EVENT:
    #         # если это одно из 3х встроенных действий:
    #         if event.object.payload.get('type') in CALLBACK_TYPES:
    #             # отправляем серверу указания как какую из кнопок обработать. Это заложено в
    #             # payload каждой callback-кнопки при ее создании.
    #             # Но можно сделать иначе: в payload положить свои собственные
    #             # идентификаторы кнопок, а здесь по ним определить
    #             # какой запрос надо послать. Реализован первый вариант.
    #             r = vk.messages.sendMessageEventAnswer(
    #                 event_id=event.object.event_id,
    #                 user_id=event.object.user_id,
    #                 peer_id=event.object.peer_id,
    #                 event_data=json.dumps(event.object.payload))
    #         # если это наша "кастомная" (т.е. без встроенного действия) кнопка, то мы можем
    #         # выполнить edit сообщения и изменить его меню. Но при желании мы могли бы
    #         # на этот клик открыть ссылку/приложение или показать pop-up. (см.анимацию ниже)
    #         elif event.object.payload.get('type') == 'my_own_100500_type_edit':
    #             last_id = vk.messages.edit(
    #                 peer_id=event.obj.peer_id,
    #                 message='ola',
    #                 conversation_message_id=event.obj.conversation_message_id,
    #                 keyboard=(keyboard_1 if f_toggle else keyboard_2).get_keyboard())
    #             f_toggle = not f_toggle