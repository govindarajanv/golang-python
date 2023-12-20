from functools import reduce

number = int(input('Enter number: ')) 


#1 lambda
factorial = lambda number: 1 if number < 2 else number * factorial(number - 1)
print('%d != %d' %(number, factorial(number)))


#The REDUCE() function implements a technique called FOLDING or reduction. It takes an existing function, applies it cumulatively to all the items in iterable, and returns a single final value
# functools.reduce(function, iterable[, initializer])

#2 Reduce 

factorial = lambda num: reduce(lambda x, y: x * y, range(1, num+1))
print('%d != %d' %(number, factorial(number)))


#3 Reduce

def compute_factorial(a,b):
    return a*b
    
print('%d != %d' %(number, reduce(compute_factorial, range(1,number+1))))

#4 Using map 

numbers = [3, 4, 6, 2, 1, 5]


def fn_factorial(number):
    if number < 2:
        return 1
    else:
        return number * fn_factorial(number - 1)


result = map(fn_factorial,numbers)
num_list = list(result)
print (num_list)

#5 filter

result = list(filter(lambda num: num % 10 == 0,num_list))
print (result)

#6 Any and all
list_of_odd = [x % 2 == 0 for x in num_list ]
print (list_of_odd)
print (f"Is there any odd number in the list {num_list}:",any(list_of_odd))
print (f"Are all the numbers odd  in the list {result}:",all(result))