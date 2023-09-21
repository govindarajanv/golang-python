import json

class Application:

   def __init__(self, app_name = None, app_type = None):
      self.app_name = app_name
      self.app_type = app_type

   def __str__(self):
      return str(self.__dict__)
		
   @classmethod
   def getAll(self):
      database = open('db.json', 'r')
      result = []
      json_list = json.load(database)
      for item in json_list:
         application = Application(item['app_name'], item['app_type'])
         result.append(application)
      return result