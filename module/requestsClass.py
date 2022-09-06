import requests
import os
# import vk_api



"""?&"""

class GKUser:

  def __init__(self):
    """
    Get Key-token for User
    :return: Key : str
    """
    self.user_token : str
    self.urlAuthorize = "https://oauth.vk.com/authorize/"

    # self.headers = {
    #   "redirect_url": "http://oauth.vk.com/blank.html"
    # }

    client_secret = os.environ("client_secret")
    self.params = {
      "client_id" : "51416002",
      "scope" : "messages.photos.friends.stories.pages.groups",
      "response_type" : "code",
      "display" : "page",
      "redirect_url": "https://oauth.vk.com/blank.html",
      "client_secret" : client_secret,

      "v" : "5.131"
    }
  def autorisation(self):
    var_requests = requests.get(url=self.urlAuthorize, params=self.params) #,

    self.user_token = var_requests

    return self.user_token

class Bases:

  def __init__(self):
    self.user_token = GKUser.autorisation(self)
    self.urlAuthorize = "https://api.vk.com/method/"
    self.user_ids : str

