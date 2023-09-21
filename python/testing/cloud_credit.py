import unittest

class CloudCredit:
  def __init__(self, id):
    self.id = id
    self.balance = 0

  def consume(self, consume):
    if self.balance >= consume:
      self.balance -= consume
      return True
    return False

  def credit(self, credit):
    self.balance += credit
    return True