from module.user_token.token_api_vk import mainAutor, renameFile
import os
import json

import vk_api
if __name__ == "__main__":

  # --------Create db--------
  # with Session(bind="postgres") as session:
  # test = sqlt(dbname = "tests5")
  # test.templateTable()

  # --------Get token and ID of usser --------
  if not os.path.exists("vk_config.json"):
    if not os.path.exists("vk_config.v2.json"):
      login, passw = input("Login: "), input("Passw: ")
      vk_session = mainAutor(login, passw)
      vk_login = vk_api.VkApi(login, passw)
      vk_login.token['access_token']

    if not os.path.exists("vk_config.json"):
      renameFile()

      with open("vk_config.json", "r") as vkv2:
        dict_var = json.load(vkv2)
        login = list(dict_var.keys())[0]
        token = dict_var[login]["token"]["app6222115"]["scope_FRIEND.STORIES.MESSAGES"]["access_token"]
        id_user = dict_var[login]["token"]["app6222115"]["scope_FRIEND.STORIES.MESSAGES"]["user_id"]

      with open("../../.env", "a") as file_env:
        file_env.write(
          """

# User_token for VK
TOKEN_API_VK = %s

# ID of autorized User     
user_id_user = %s
""" % (token, id_user)
    )

  else:
    if not os.path.exists("vk_config.json"):
      renameFile()



  # --------....--------
  #   user = apiFunction(token, int(id_user))
  #   us = user.getUser()
  #   print(us)

