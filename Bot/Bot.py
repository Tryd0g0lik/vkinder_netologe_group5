import vk_api
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

class Bot():
    #инициализация класса Bot
    def __init__(self, token_bot, group_id):
        self.token = token_bot
        self.group_id = group_id
        self.command = {
            'start',
            'help',
            'next',
            'back',
            'search',
            'filter',
            'favorites',
            'blacklist'}

        vk_session = vk_api.VkApi(token=token_bot)
        self.longpoll = VkBotLongPoll(vk_session, group_id)
        vk = vk_session.get_api()

    #метод событие новое
    def message_new(self, event):
        ...
    #метод событий
    def message_event(self, event):
        ...