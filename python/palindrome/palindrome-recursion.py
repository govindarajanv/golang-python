def isPalindrome(s):
 
    # to change it the string is similar case
    s = s.lower()
    l = len(s)
    if l < 2:
        return True
    elif s[0] == s[l - 1]:
        # Call is palindrome form substring(1,l-1)
        return isPalindrome(s[1: l - 1])
    else:
        return False
 
# Driver Code
s = input("Enter the string:")
if isPalindrome(s):
    print("Yes")
else:
    print("No")