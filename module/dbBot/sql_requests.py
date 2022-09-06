import requests
import os
from config import CLIENT_SECRET, LOGIN_DB, PASSWORD_DB
import psycopg2
import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, String, Integer, Text, Column, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
import inspect

class Botdb():
  def __init__(self, id_user = None, id_elected_user = None,
               id_status = None):
    self.id_elected_user = id_elected_user
    self.id_user = id_user
    self.id_status = id_status
    self.conn = psycopg2.connect(database="vkinder", user=LOGIN_DB, password=PASSWORD_DB)
    self.cur = self.conn.cursor()

  def __close(self):
    self.conn.close()
    self.cur.close()

  def selectData(self):

    self.cur.execute("""SELECT * FROM elected_users;""")
    response_select = self.cur.fetchall()

    self.conn.rollback()
    Botdb.__close(self)

    return response_select

  def insertlected(self):

    self.cur.execute("""\
INSERT INTO elected_users VALUES (%s, %s,%s);"""
% (self.id_user, self.id_elected_user, self.id_status))
    self.conn.commit()
    Botdb.__close(self)
    return

  def insertUser(self, params : list):

    self.cur.execute(
        """INSERT INTO users VALUES (%s,'%s','%s',%s,%s,'%s');""" % (
          params["id_vk"], params["first_name"],
          params["last_name"], params["age"],
          params["id_sity"], params["tokens"])
        )

    self.conn.commit()
    Botdb.__close(self)
    return

t = Botdb()
# t.insertlected()
print(t.selectData())

class sqlTasks():
  def __init__(self, dbname,  password = "nlo7"):
    """
    :param dbname: Receiving database-name and creating base.
    :param password: 'password' variable has from password default the 'nlo7'

    def __exists() - checking:
      - True if dataBase-name be exists
      - False if not exists
    def __connectedPosgres() - connecting with a 'db-postgres'
    def __createdb() - Build new data-base if it not exists
    def connectionNewDB() - The buil connection for a new database.
    def templateTable() - The created templates for a new-db and returned tables from this's new db
    :return: True or False

    """

    self.dbname = dbname
    self.password = password

  def __connectedPosgres(self):
    """
    Basic requests the db-postgres default
    """
    return create_engine("postgresql://postgres:%s@localhost:5432/postgres" % (self.password, ))

  def __createdb(self):
    """
    :return: Build new data-base if it not exists
    """
    session = sqlTasks.__connectedPosgres(self)

    with session.connect() as conn:
      conn.execute("commit")

    url = 'postgresql://postgres:%s@localhost:5432/%s' % (self.password, self.dbname )
    if not sqlTasks.__exists(self):
      create_database(url)
      print("Created database!")
    else:
      print("""DataBase exists. Session is closing""")
      conn.close()

      return

      exit()

    conn.close()
    print("Session closed!")


    return

  def __exists(self):
    """
    :param dbname: dataBase-name checking:
      - True if dataBase-name be exists
      - False if not exists
    :return: True or False
    """
    return database_exists('postgresql://postgres:%s@localhost:5432/%s' % (self.password, self.dbname ))

  def connectionNewDB(self):

    """
    :return: The buil connection for a new database.
    """
    sqlTasks.__createdb(self)

    return create_engine("postgresql://postgres:%s@localhost:5432/%s" % (self.password, self.dbname ))


  def templateTable(self):
    """
    :return: The created templates for a new-db and returned tables from this's new db
    """

    metadata = MetaData()
    engine = sqlTasks.connectionNewDB(self)

    users = Table(
      'users', metadata,
      Column('id_vk', Integer(), primary_key=True),
      CheckConstraint('id_vk >= 1' and 'id_vk <= 9999999999', name='id_check'),
      Column('first_name', String(20), nullable=False),
      Column('last_name', String(20), nullable=False),
      Column('age', Integer(), default=18),
      CheckConstraint('age >= 18' and 'age <= 99', name='user_age'),
      Column('id_sity', Integer(), nullable=False),
      Column('tokens', String(150), nullable=False)
    )

    filters = Table(
      'filters', metadata,
      Column('id', Integer(), primary_key = True),
      Column('code_filter', String(50))
    )

    status = Table(
      'status', metadata,
      Column('id', Integer(), primary_key = True),
      Column('type_status', String(12), default='defauList')
    )

    elected_user = Table(
      'elected_users', metadata,
      Column('id_user', sqlalchemy.ForeignKey("users.id_vk") ),
      Column('id_elected_user', Integer()),
      CheckConstraint('id_elected_user >= 1' and 'id_elected_user <= 9999999999', name='id_elected_user'),
      Column('id_status', sqlalchemy.ForeignKey("status.id"))

    )
    metadata.create_all(engine)
    return (users, filters, status, elected_user)




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