import random
# set the success flag to false
success = False

# Generate random number
target = random.randint(0,100)

print ("We have chosen a number. can you guess it?")

guesses = 0
for i in range(10):
    print ("\nYou have ",10-guesses," left")
    inp = input("Enter your guess:")
    guesses += 1
    try: 
        guess = int(inp)
    except:
        print ("Exception has occurred")
    if guess < target:
        print ("your guess is low")
    elif guess > target:
        print ("your guess is high")
    else:
        print ("You have guessed it right")
        break






