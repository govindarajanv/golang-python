#  separate algorithms from the objects on which they operate
class AppRelease:
    def involve(self, visitor):
        visitor.visit(self)
    def develop(self, visitor):
        print(self, "Developed by", visitor)
    def automate(self, visitor):
        print(self, "Automated by", visitor)
    def audit(self, visitor):
        print(self, "Audited by", visitor)
    def __str__(self):
        return self.__class__.__name__
 
# Concrete Crops: Classes being visited.
class Frontend(AppRelease): pass
class Backend(AppRelease): pass

 
# Abstract Visitor class for Concrete Visitor classes: method defined in this class will be inherited by all Concrete Visitor classes.
class Visitor:
    def __str__(self):
        return self.__class__.__name__
 
# Concrete Visitors: Classes visiting Concrete Crop objects. These classes have a visit() method which is called by the accept() method of the Concrete Crop classes.
class Developer(Visitor):
    def visit(self, release):
        release.develop(self)
 
class DevOps(Visitor):
    def visit(self, release):
        release.automate(self)
 
class InfoSec(Visitor):
    def visit(self, release):
        release.audit(self)
 
### USING THE ABOVE SETUP ###
# Creating apps
web_portal = Frontend()
registration_service = Backend()
 
# Creating Visitors
ram = Developer()
prem = DevOps()
nakul = InfoSec()
 
# Visitors visiting Plants
web_portal.involve(ram)
web_portal.involve(prem)
web_portal.involve(nakul)
 
registration_service.involve(ram)
registration_service.involve(prem)
registration_service.involve(nakul)
