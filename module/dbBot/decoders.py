
from module.dbBot.sql_requests import Botdb
from sqlalchemy.orm import declarative_base
import inspect

from sqlalchemy_utils.types.pg_composite import psycopg2

from config import LOGIN_DB, PASSWORD_DB


"""
This's functions for jobs between vk-bot and db
"""





def User(func):
	"""
	"\module\API_VK\api.py : def user()"
	:param func: Id user
	:return: list of data went authorized users
	"""
	def new_function(self, user_id):
		res = func(self, user_id)
		print("111", res)
		params = {
			"id_vk" : res["id"],
			"first_name" : res["first_name"],
			"last_name" : res["last_name"],
			"age" : 18,
			"id_sity" : res["city"]['id'],
			"tokens" : "Null"
		}

		users_table = Botdb()
		users_table.insertUser(params)


		return params
	return  new_function




def Blacklist(func : object):
	def new_function(*args ):
		responseList = func(*args)
	return








