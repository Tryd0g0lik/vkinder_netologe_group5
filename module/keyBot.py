from module.user_token.token_api_vk import checkInput
import os
class BasisKey:
	"""
	KEyword create in a file for '.env'.
	"""
	def __init__(self):
		print("Insert db name of  a bot db name ")
		self.db_name = checkInput()
		print("Key of your app for work in API")
		self.token_bot = checkInput()
		print("Group id")
		self.group_id = checkInput()
		print("Login_db")
		self.client_secret = checkInput()
		print("Login_db")
		self.login_db = checkInput()
		print("Password_db")
		self.password_db = checkInput()

	def keys(self):
		env_var = """
# Connect to the DB
DSN=postgresql://postgres:password@localhost:5432/%s

# Key of your app for work in API
TOKEN_BOT=%s

# Group_Id
GROUP_ID=%s

# Version for the Api Vk
VERSION_API_VK=5.131

# Защищённый ключ
CLIENT_SECRET = %s

# the data for connecte with database
# login of db
LOGIN_DB = %s

#Password of db
PASSWORD_DB = %s


# User_token for VK
# ID of autorized User


""" % (self.db_name, self.token_bot,
		   self.group_id, self.client_secret, self.login_db, self.password_db)

		if not os.path.exists("../.key"):
			with open("../.key", "a") as file:
				file.write("%s" %(env_var, ))

		return
