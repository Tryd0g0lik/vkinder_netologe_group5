# from ..Bot.FuncBot import message_new
from ...main1 import function_send
from sqlalchemy import create_engine
from postgrasclass import sqlTasks
import psycopg2
from ...config import LOGIN_DB, PASSWORD_DB

# "postgresql+psycopg2://%s:%s@loccalhost/vkinder" % (LOGIN_DB, PASSWORD_DB)
if __name__ == "__main_dbot__":
	conn = psycopg2.connect(database="vkinder", user = LOGIN_DB, password = PASSWORD_DB)
	with conn.cursor() as cur:
		cur.execute("INSERT INTO users (first_name, last_name, age, id_sity, tokens)"\
		            VALUES())



