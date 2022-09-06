import sqlalchemy
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine, MetaData, Table, String, Integer, Text, Column, CheckConstraint
from sqlalchemy.ext.declarative import declarative_base
import inspect

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



f = sqlTasks(dbname="vkinder")
print(f.templateTable())
