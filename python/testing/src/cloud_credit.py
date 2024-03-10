class CloudCredit:

    def __init__(self,id):
        self.id = id
        self.balance = 0

    def consume(self,consume):
        if self.balance >= consume:
            self.balannce -= consume
            return True
        return False

    def credit(self, credit):
        if credit >= 0:
            self.balance += credit
            return True
        return False

    def discount(self,code):
        if code in ['DISCBFRIDAY','DSICCYBMONDAY']:
            self.balance += 500
            return True
        return False