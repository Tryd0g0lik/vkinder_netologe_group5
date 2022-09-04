import json
import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.utils import get_random_id
from config import DSN, TOKEN_BOT, TOKEN_API_VK, VERSION_API_VK, GROUP_ID
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from API_VK.api import api

class vkBot():
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=TOKEN_BOT)
        self.longpoll = VkBotLongPoll(self.vk_session, GROUP_ID)
        self.vk = self.vk_session.get_api()

    def menu_keyboard(self):
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
        return keyboard

    def menu_search(self):
        keyboard_sender = VkKeyboard(inline=True)
        keyboard_sender.add_callback_button(label='⬅', color=VkKeyboardColor.SECONDARY,
                                            payload={"type": "search_back"})
        keyboard_sender.add_callback_button(label='❌ Черный список', color=VkKeyboardColor.PRIMARY,
                                            payload={"type": "add_blacklist"})
        keyboard_sender.add_callback_button(label='❤ Избранный', color=VkKeyboardColor.POSITIVE,
                                            payload={"type": "add_favorites"})
        keyboard_sender.add_callback_button(label='➡', color=VkKeyboardColor.SECONDARY,
                                            payload={"type": "search_next"})
        return keyboard_sender

    def message(self, peer_id, random_id, message, keyboard=None, attachment=None):
        if keyboard is not None:
            keyboard = keyboard.get_keyboard()
        else:
            keyboard = ''
        if attachment is not None:
            attachment = attachment
        else:
            attachment = ''
        return self.vk.messages.send(
            peer_id=peer_id,
            random_id=random_id,
            keyboard=keyboard,
            message=message,
            attachment=attachment
        )

    def bot_help_message(self):
        message = f"Справка по командам:\n" \
                  f"help - справка\n" \
                  f"start - начать работу с ботом\n" \
                  f"search - поиск пользователей по заданному фильтру\n" \
                  f"search_next - поиск, листать Далее\n" \
                  f"search_back - поиск, листать Назад\n" \
                  f"filter - настройка фильтра поиска\n" \
                  f"filter_setting 99,2,6,20,23 - изменить настройки фильтра\n" \
                  f"add_favorites - добавить пользователя в избранные\n" \
                  f"add_blacklist - добавить потльзователя в чёрный список\n" \
                  f"favorites - список избранных пользователей\n" \
                  f"blacklist - список пользователей попавших в черный список"
        return message