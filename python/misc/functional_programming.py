import functools,operator

numbers = [9, 3, 49, 6, 28, 5, 20, 0, 3, 7,4, 2, 23, 34, 1, 8, 35]

# create a list with odd numbers > 7 using list comprehension
odd_gt_7 = [num if num > 7 else 0 for num in numbers if num % 2 != 0 ]
print ("odd_gt_7",odd_gt_7)

# Create a list of square of all numbers in the original list using map
squares = list (map(lambda num: num ** 2,numbers))
print ("squares",squares)

# create a list with even numbers less than 7 from the original list with filter function
even_lt_7 = list(filter(lambda num: num % 2 == 0 and num < 7,numbers))
print ("even_lt_7",even_lt_7)

# create a sum of all numbers in the original list
sum = functools.reduce(lambda x,y:x+y,numbers)
print (sum)

strings = ["Learning"," Python"," Is"," Fun"]

# Use join to concatenate strings
print (''.join(strings))

# Use functools.reduce to concatenate strings
print (functools.reduce(lambda x,y:x+y,strings))

# use operator.add to concatenate strings
print (functools.reduce(operator.add,strings))

strings = ["Learning"," Python","In","2023"," Is"," Fun"]

# check if there is any num in strings list
check_num = [x.isnumeric() for x in strings]
print ("any number?",any(check_num))
print ("all numbers?",all(check_num))



