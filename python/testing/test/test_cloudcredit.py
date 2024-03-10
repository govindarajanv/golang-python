from src.cloud_credit import *                                                                                                                                           

def test_insufficient_credits():

  a = CloudCredit(1)
  a.credit(100)

  outcome = a.consume(200)

  assert outcome == False

def test_negative_credits():

  a = CloudCredit(1)

  outcome = a.credit(-100)

  assert outcome == False

def test_discount():
    a = CloudCredit(1)

    outcome = a.discount("DUMMY")
    assert outcome == False

    outcome = a.discount("DISCBFRIDAY")
    assert outcome == True