def bracketsBalanced(value):
    stack = []
    for c in value:
        if c in "{[(":
            stack.append(c)
            print (stack)
        elif c in "}])":
            stack.pop()
            print (stack)
    print (stack)


if __name__ == "__main__":
    test = "{[{}[()]}]"
    print (bracketsBalanced(test))