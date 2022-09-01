from sqlalchemy_utils import database_exists, create_database
from sqlalchemy import create_engine

class sqlTasks:
  def __init__(self, dbname,  password = "nlo7"):
    self.dbname = dbname
    self.password = password

  def connectedPosgres(self):
    """
    Basic requests the db-postgres default
    """
    return create_engine("postgresql://postgres:nlo7@localhost:5432/postgres")

  def __exists(self):
    """
    :param dbname: get dataBase-name and checking:
      - True if dataBase-name be exists
      - False if not exists
    :return: True or False
    """
    return database_exists('postgresql://postgres:nlo7@localhost:5432/%s'%(self.dbname ,))



  def createdb(self):
    """
    :param dbname: Geting database-name and creating base
    :return: Null.
    """

    session = sqlTasks.connectedPosgres(self)
    with session.connect() as conn:
      conn.execute("commit")
    url = 'postgresql://postgres:%s@localhost:5432/%s' % (self.password, self.dbname )

    if not sqlTasks.__exists(self):
      create_database(url)
      print("Created database!")
    conn.close()
    print("Session closed!")
    return
  def connectionNewDB(self):
    ...


  def create(self):
    ...
  def insesert(self):
    ...
