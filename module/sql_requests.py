import requests
import os
from config import CLIENT_SECRET, LOGIN_DB, PASSWORD_DB
import psycopg2




"""?&"""

# class GKUser:
#
#   def __init__(self):
#     """
#     Get Key-token for User
#     :return: Key : str
#     """
#     self.user_token : str
#     self.urlAuthorize = "https://oauth.vk.com/authorize/"
#
#     # self.headers = {
#     #   "redirect_url": "http://oauth.vk.com/blank.html"
#     # }
#
#     client_secret = os.environ("client_secret")
#     self.params = {
#       "client_id" : "51416002",
#       "scope" : "messages.photos.friends.stories.pages.groups",
#       "response_type" : "code",
#       "display" : "page",
#       "redirect_url": "https://oauth.vk.com/blank.html",
#       "client_secret" : client_secret,
#
#       "v" : "5.131"
#     }
#   def autorisation(self):
#     var_requests = requests.get(url=self.urlAuthorize, params=self.params) #,
#
#     self.user_token = var_requests
#
#     return self.user_token

# class Bases:
#
#   def __init__(self):
#
#     self.urlAuthorize = "https://api.vk.com/method/"
#     self.user_ids : str
#     self.params = {
#       "client_id" : "51416002",
#       "scope" : "messages.photos.friends.stories.pages.groups",
#       "response_type" : "code",
#       "display" : "page",
#       "redirect_url": "https://oauth.vk.com/blank.html",
#       "client_secret" : CLIENT_SECRET,
#
#       "v" : "5.131"
#     }
class Basis:
  def __init__(self):
    self.conn = psycopg2.connect(database="vkinder", user=LOGIN_DB, password=PASSWORD_DB)
    self.cur = self.conn.cursor()

class Botdb():
  def __init__(self, id_user = None, id_elected_user = None,
               id_status = None):
    self.id_elected_user = id_elected_user
    self.id_user = id_user
    self.id_status = id_status
    self.conn = psycopg2.connect(database="vkinder", user=LOGIN_DB, password=PASSWORD_DB)
    self.cur = self.conn.cursor()

  def selectData(self):

    self.cur.execute("""SELECT * FROM elected_users;""")
    response_select = self.cur.fetchall()

    self.conn.rollback()
    self.conn.close()
    self.cur.close()

    return response_select

  def insertlected(self):

    self.cur.execute("""\
INSERT INTO elected_users VALUES (%s, %s,%s);"""
% (self.id_user, self.id_elected_user, self.id_status))
    self.conn.commit()
    self.conn.close()
    self.cur.close()
    return

  def insertUser(self, params : list):

    self.cur.execute(
        """INSERT INTO users VALUES (%s,'%s','%s',%s,%s,'%s');""" % (
          params["id_vk"], params["first_name"],
          params["last_name"], params["age"],
          params["id_sity"], params["tokens"])
        )

    self.conn.commit()
    self.conn.close()
    self.cur.close()
    return

t = Botdb()
# t.insertlected()
t.selectData()