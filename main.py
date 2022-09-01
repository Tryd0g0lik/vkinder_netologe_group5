from sqlalchemy import create_engine
from sqlalchemy.engine import url
import psycopg2
from sqlalchemy.orm import Session
from functions import dbConnection
from postgrasclass import sqlTasks as sqlt

if __name__ == "__main__":



    # with Session(bind="postgres") as session:
  test = sqlt(dbname = "client")
  test.createdb()



