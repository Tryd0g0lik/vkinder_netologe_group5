from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType
from module.Bot.vkBot import vkBot
from module.user_token.token_api_vk import token, checkInput


class Topmenu:

    def topMenu(self):
        """
        :return: Basis menu
        """
        return """
       Select the symbol for launch application:
        - 't' get a user-token;
        - 's' start a Bot.       
        - 'e' exit
        
        """

    def insert(self):
        """
        :return: Return one symbol for a launch command of an application
        """

        print("Choose a command.")
        response  = ((checkInput())[0]).lower()

        if response in "t":
            token()
        elif response in "s":
            bot = vkBot()
            for event in bot.longpoll.listen():
                random_id = get_random_id()
                if event.type == VkBotEventType.MESSAGE_NEW:
                    peer_id = event.object.message['peer_id']
                    event_command = event.object.message['text'].lower()
                    bot.bot_command(event_command, event, peer_id, random_id)

                elif event.type == VkBotEventType.MESSAGE_EVENT:
                    peer_id = event.object.peer_id
                    event_command = event.object.payload['type']
                    bot.bot_command(event_command, event, peer_id, random_id)
        elif response in "e":
            exit()
        else:
            return

if __name__ == "__main__":
    while True:
        menu = Topmenu()
        print(menu.topMenu())
        menu.insert()


