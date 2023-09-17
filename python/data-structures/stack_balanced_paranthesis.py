import stack_using_list

def isParanthesisBalanced(text):
    stack = stack_using_list.Stack()

    for ch in text:
        if ch in "{[(":
            stack.push(ch)
        elif ch in "}])":
            stack.pop()
    return len(stack) == 0

if __name__ == "__main__":
    text = input("Enter the text to check if parantheses are balanced: ")
    if isParanthesisBalanced(text):
        print ("Parantheses are balanced")
    else:
        print ("Parantheses aren't balanced")

        