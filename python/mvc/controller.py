from model import Application
import view

def fetch():
   #gets list of all Application objects
   applications_in_db = Application.fetchAll()
   
   #calls view
   return view.renderView(applications_in_db)

def start():
   view.startView()
   input_val = input()
   if input_val == 'y':
      return showAll()
   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()
