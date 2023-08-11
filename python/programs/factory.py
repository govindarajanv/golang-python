class Tea:

    def __init__(self,flavour="Plain"):
        self.flavour = flavour

    def consume(self):
        print (f"{self.flavour} Tea is getting consumed")

class TeaFactory:

    @staticmethod
    def prepare(flavour="Plain"):
        print (f"{flavour} Tea is getting prepared")
        return Tea(flavour)

if __name__ == "__main__":
    tea = TeaFactory.prepare()
    print (tea.consume())
    tea = TeaFactory.prepare("Ginger")
    print (tea.consume())
