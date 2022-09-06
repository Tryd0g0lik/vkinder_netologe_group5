from sqlalchemy.orm import declarative_base
import inspect
"""
This's functions for jobs between vk-bot and db
"""


def User(func):
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





