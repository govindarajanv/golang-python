from model import Application

def renderView(list):
   print ('\nIn our db we have %i apps. Below is the list:' % len(list))
   for item in list:
      print (item)

def startView():
   print ('A simplest MVC Implementation')
   print ('Do you want to see applications in my App Catalog?[y/n]')

def endView():
   print ('Exiting!')
