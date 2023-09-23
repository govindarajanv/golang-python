import unittest
from cloud_credit import *

class TestCloudOperations(unittest.TestCase):
    def test_insufficient_deposit(self):

      a = CloudCredit(1)
      a.credit(100)
      outcome = a.consume(200)

      self.assertFalse(outcome)
    
    def test_negative_deposit(self):
        a = CloudCredit(1)
        outcome = a.credit(-100)

        self.assertFalse(outcome)