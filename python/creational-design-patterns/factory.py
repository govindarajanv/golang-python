# define Python user-defined exceptions

class Tea:

    def consume(self):
        print ("Tea is getting consumed")

class TeaFactory:

    @staticmethod
    def prepare():
        print ("Tea is getting prepared")
        return Tea()

if __name__ == "__main__":
    tea = TeaFactory.prepare()
    print (tea.consume())
