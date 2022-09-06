from sqlalchemy.orm import declarative_base
import inspect
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
		return params
	return  new_function

def listFivorites(func : object):
	def new_function(*args ):
		response_fivorites = func(*args)







