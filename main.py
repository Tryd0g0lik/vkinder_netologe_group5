from module.postgrasclass import sqlTasks as sqlt
from module.requestsClass import GKUser as gku
import webbrowser
import vk_api
if __name__ == "__main__":


  # with Session(bind="postgres") as session:
  # test = sqlt(dbname = "tests5")
  # test.templateTable()

  testUser = gku()
  testUser.autorisation()


