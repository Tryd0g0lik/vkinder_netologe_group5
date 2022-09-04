import requests
# import vk_api

import tokenVk

"""?&"""

class GKUser:

  def __init__(self):
    """
    Get Key-token from User
    :return: Key : str
    """
    self.user_token : str
    self.urlAuthorize = "https://oauth.vk.com/authorize/"

    # self.headers = {
    #   "redirect_url": "http://oauth.vk.com/blank.html"
    # }
    self.header = {

      "pass": "OBD0P1QEk47NsnO4NhAkVaEROVCCBN",
      "email": "work80@mail.ru"
    }
    self.params = {
      "client_id" : "51416002",
      "scope" : "messages.photos.friends.stories.pages.groups",
      "response_type" : "code",
      "display" : "page",
      "redirect_url": "https://oauth.vk.com/blank.html",
      "client_secret": "ZlKhq1rIGnRGDBvCFdWM",

      "v" : "5.131"
    }
  def autorisation(self):
    var_requests = requests.get(url=self.urlAuthorize, params=self.params, headers=self.header) #,
    # headers=self.headers
    # var_requests = requests.get("""https://oauth.vk.com/authorize/?client_id=51416002&scope=messages.photos.friends.stories.pages.groups&response_type=token&display=page&redirect_url=https://oauth.vk.com/blank.html&v=5.131""")
    self.user_token =var_requests #.url #.split("=").pop(-2)[ : -2]
    print(self.user_token)

    # https://oauth.vk.com/authorize/?client_id=51416002&scope=messages.photos.friends.stories.pages.groups&response_type=code&display=popup&redirect_url=https://oauth.vk.com/blank.html&v=5.131
    # https://oauth.vk.com/authorize?client_id=1&redirect_uri=http://example.com/callback&scope=12&display=mobile
    var_requests
    return self.user_token

class Bases:

  def __init__(self):
    self.user_token = GKUser.autorisation(self)
    self.urlAuthorize = "https://api.vk.com/method/"
    self.user_ids : str

