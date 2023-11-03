class PythonCLI:
    def execute(self, filename):
        print("executing program file:", filename)

class AnsibleCLI:
    def execute(self, filename):
        print("executing playbook file:", filename)

class TerraformCLI:
    def execute(self, filename):
        print("executing configuration file:", filename)

class JenkinsPipelineStep:
    def __init__(self):
        self.tf = TerraformCLI()
        self.ansible = AnsibleCLI()
        self.python = PythonCLI()

    def execute(self, filename):
        if filename.endswith(".tf"):
            self.tf.execute(filename)
        elif filename.endswith(".yml"):
            self.ansible.execute(filename)
        elif filename.endswith(".py"):
            self.python.execute(filename)
        else:
            print("Unsupported file format.")

# Client code
step = JenkinsPipelineStep()
step.execute("playbook.yml")
step.execute("main.tf")
step.execute("ec2_boto.py")