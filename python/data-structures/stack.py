from collections import deque

stack = deque()

print ("Adding to the stack")

for i in range(0,5):
    item = input("Enter the item:")
    stack.append(item)
    print ("Stack contents",stack)


print ("Removing from the stack")

for i in range(0, len(stack)):
    stack.pop()
    print ("Stack contents",stack)

try:
    x = 1/0
    stack.pop()
except IndexError:
    print ("Stack is empty")
except Exception as error:
    print ("Other error", type(error).__name__)
else:
    print ("Stack is not empty")
finally:
    print ("Stack Implementation is complete")