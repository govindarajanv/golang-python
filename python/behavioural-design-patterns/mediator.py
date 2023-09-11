# reduce chaotic dependencies between objects. The pattern restricts direct communications between the objects and forces them to collaborate only via a mediator object
class SlackChannel:
    '''Mediator class.'''
    def sendMessage(self, user, message):
        print("[{} says]: {}".format(user, message))
 
class User:
    '''A class whose instances want to interact with each other.'''
    def __init__(self, name):
        self.name = name
        self.channel = SlackChannel()
 
    def sendMessage(self, user, message):
        self.channel.sendMessage(self,message)
 
    def __str__(self):
        return self.name
 
developer = User("Dev-User")
devOps = User("DevOps-User")
infoSec = User("InfoSec-User")
 
developer.sendMessage(devOps,"please fix the infra issue")
devOps.sendMessage(developer,"Infra issue is fixed. App is ready for the release")
developer.sendMessage(infoSec, "I need InfoSec's approval for the release")
infoSec.sendMessage(developer,"Approved")
developer.sendMessage(devOps,"Release the feature")
devOps.sendMessage(developer,"Feature is released in Prod")