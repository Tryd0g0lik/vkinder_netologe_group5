import vk_api
from config import TOKEN_BOT, GROUP_ID
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from module.Bot.FuncBot import message_new, message_event
# from module.dbBot.dbot import Basis

vk_session = vk_api.VkApi(token=TOKEN_BOT)

longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()

command = {'start', 'help', 'next', 'back', 'search', 'filter', 'favorites', 'blacklist'}
message_id = 0

for event in longpoll.listen():
    if event.type == VkBotEventType.MESSAGE_NEW:
        print(f"MESSAGE_NEW ========>  {event}")
        if event.object.message['text'].lower() in command:
            tuple_var = message_new(event.object.message, event, vk)
            def function_send():
                return tuple_var
    elif event.type == VkBotEventType.MESSAGE_EVENT:
        print(event)
        print(f"{event.object.conversation_message_id}================={event.object.peer_id}")

        print(f"MESSAGE_ID = {message_id}")
        message_event(message_id, event, vk)
