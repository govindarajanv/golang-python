def reverse(str):
    str_type = type(str) 
    empty_str = str_type()
    if (str == empty_str):
        return empty_str
    
    rest = reverse(str[1:])
    first = str[0:1]
    return  rest + first
    
if __name__ == "__main__":
    str = input("Enter the string:")
    print ("Using Reflections")
    if str == reverse(str):
        print ("{} is a palindrome".format(str))
    else:
        print ("{} is not a palindrome".format(str))

    print ("Pythonic way")
    if str == str[::-1]:
        print ("{} is a palindrome".format(str))
    else:
        print ("{} is not a palindrome".format(str))
