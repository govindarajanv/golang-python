class JobDescriptor:
    def __init__(self):
        self.__build_timeout = 0
    def __get__(self, instance, owner):    
        return self.__build_timeout
    def __set__(self, instance, value):
        if isinstance(value, int):
            pass
        else:
            raise TypeError("Build timeout can only be an integer")

        if value < 0:
            raise ValueError("Build timeout can never be less than zero")

        self.__build_timeout = value

    def __delete__(self, instance):
        del self.__build_timeout

class CIBuild:
    build_timeout = JobDescriptor()
    def __init__(self,workflow_name,timeout):
        self.workflow_name = workflow_name
        self.build_timeout = timeout
        self.status = "Created"

    def __str__(self):
        return "Workflow {0} with a build timeout of {1} is created.".format(self.workflow_name,self.build_timeout)
if __name__ == "__main__":
    build = CIBuild("new-service",20)
    print (build)
    print ("Updating the timeout")
    build.build_timeout = 40
    print (build)