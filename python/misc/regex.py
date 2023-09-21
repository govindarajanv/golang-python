import re
def validate_name(string):
    only_alpha = re.compile(r'[^a-zA-Z]')
    string = only_alpha.search(string)
    return not bool(string)

def validate_name(string):
    only_alpha = re.compile(r'[^a-zA-Z]')
    string = only_alpha.search(string)
    return not bool(string)

def look_for_failure(string):
    value = re.match ("(\w+) (\w+)", string)
    print (value.groups())
    
    print (re.findall(r"(\w+) (\w+)", string))
    #r1 = re.findall(r"^\w+",string)
    failure = re.search(r'fail')
    return not bool(failure)
    
print(validate_name("ABCDEFabcdef")) 
print(validate_name("*&%@#!}{"))

test_str = "fail there is some error."
value = re.match ("(\w+) (\w+)", test_str)
print ("groups:",value.groups())
print ("findall:",re.findall(r"(\w+) (\w+)", test_str))
result = re.search(r'fail',test_str)
print ("search:",result.group(0))