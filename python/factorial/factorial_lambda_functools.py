from functools import reduce

def compute_factorial(a,b):
    return a*b


number = int(input('Enter number: ')) 

# method 1
factorial = lambda num : 1 if num < 2 else num * factorial (num -1)
print('%d != %d' %(number, factorial(number)))

# method 2
factorial = lambda num: reduce(lambda x, y: x * y, range(1, number+1))
print('%d != %d' %(number, factorial(number)))

# method 3
print('%d != %d' %(number, reduce(compute_factorial, range(1,number+1))))