import bcrypt
import hashlib


set_password = b'Hard2Gu335!'

method = int(input("choose the method: 0 - bcrypt, 1 - hashlib"))
guess = input("Enter your guess for the password")

if method == 0:
    set_hashed = bcrypt.hashpw(set_password, bcrypt.gensalt())
    if bcrypt.hashpw(guess.encode('utf-8') , set_hashed) == set_hashed:
        print ("You have guessed it right")
    else:
        print ("Your guess is wrong")
elif method == 1:
    set_hashed = hashlib.sha512(set_password)
    guess = hashlib.sha512(guess.encode('utf-8'))
    if guess.hexdigest() == set_hashed.hexdigest() :
        print ("You have guessed it right")
    else:
        print ("Your guess is wrong")