class VM:

    def __init__(self,name):
        self.name = name
        self.image = None
        self.cpu = None
        self.disk = None
        self.memory = None

    def __str__(self):
        return f"{self.name}, {self.image}, {self.cpu} CPUs, {self.disk} Disk, {self.memory} RAM"

class VMBuilder:
    def __init__(self,name):
        self.VM = VM(name)
    
    def configure_image(self,image):
        self.VM.image = image

    def configure_cpu(self,cpu):
        self.VM.cpu = cpu

    def configure_memory(self,memory):
        self.VM.memory = memory

    def configure_disk(self,disk):
        self.VM.disk = disk

# Director
class CLI:
    def __init__(self):
        self.builder = None

    def build_vm(self,name):
        self.builder = VMBuilder(name)
        self.builder.configure_cpu("2")
        self.builder.configure_disk("100GB")
        self.builder.configure_image("ami123456")
        self.builder.configure_memory("16GB")
    
    # The user can use now use the function the attribute 
    @property
    def VM(self):
        return self.builder.VM

if __name__ == "__main__":
    cli = CLI()
    cli.build_vm("ec2")

    print (cli.VM)



