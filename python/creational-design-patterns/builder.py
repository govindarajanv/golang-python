class VM:
    def __init__(self,name):
        self.name = name
        self.cpu = None
        self.memory = None
        self.disk = None
        self.image = None
    
    def __str__(self):
        return f"{self.name} VM created with CPU: {self.cpu}, Memory: {self.memory}, Disk: {self.disk}, Image: {self.image}"
        
class VMBuilder:
    
    def __init__(self,name):
        self.vm = VM(name)
        
    def configure_image(self,image):
        self.vm.image = image
        
    def configure_cpu(self,cpu):
        self.vm.cpu = cpu
        
    def configure_memory(self,memory):
        self.vm.memory = memory
        
    def configure_disk(self,disk):
        self.vm.disk = disk

# Director        
class CLI:
    
    def __init__(self):
        self.builder = None
        
    def build_vm(self,name,image,disk,memory,cpu):
        self.builder = VMBuilder(name)
        
        self.builder.configure_image(image)
        self.builder.configure_disk(disk)
        self.builder.configure_memory(memory)
        self.builder.configure_cpu(cpu)
    
    @property
    def VM(self):
        return self.builder.vm
        
if __name__ == "__main__":
    
    awscli = CLI()
    awscli.build_vm("ec2","Amazon Linux","500 GB","16 GB","2 cores")
    print (awscli.VM)
    awscli.build_vm("ec2","CentOS","200 GB","32 GB","4 cores")
    print (awscli.VM)  



