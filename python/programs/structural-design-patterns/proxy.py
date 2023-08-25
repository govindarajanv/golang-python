from abc import ABC, abstractmethod

class Payment:
    
    @abstractmethod
    def process_payment(self, amount):
        pass


class DebitCard(Payment):

    def __init__(self,account):
        self.__account = account

    def process_payment(self,amount):
        return self.__account.process_payment(amount)

    def limit(self):
        return self.__account.balance()

class Account(Payment):

    def __init__(self,balance=0.00):
        self.__balance = balance

    def has_funds(self,amount):
        if amount > self.__balance:
            return False
        else:
            return True
    def process_payment(self, amount):
        if self.has_funds(amount):
            self.__balance = self.__balance - amount
            return True
        else:
            return False
    def balance(self):
        return self.__balance

class TapNPay:

    def swipe_card(self, card, amount):
        if card.process_payment(amount):
            print (f"Transaction for {amount} processed successfully")
            return True
        else:
            print (f"Transaction for {amount} failed")
            return False

if __name__ == "__main__":
    account = Account(1500)
    card = DebitCard(account)
    
    card_reader = TapNPay()

    print (card_reader.swipe_card(card,1300))
    print (card.limit())
    print (card_reader.swipe_card(card,1000))
    print (card.limit())