class Tea:
    
    def consume(self):
        print ("Tea is getting consumed")

class TeaFactory:

    @staticmethod
    def prepare():
        print ("Preparing Tea")
        return Tea()

if __name__ == "__main__":
    tea = TeaFactory.prepare()
    print (tea.consume())
