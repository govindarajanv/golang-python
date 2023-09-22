import re

class PatternFinder:
    
    def __init__(self, text):
        self.__text = text
    
    def find_begin(self,pattern):
        match_object = re.match(pattern, self.__text)
        if match_object:
            print("Match found!")
        else:
            print("No match found!")
 
    def find_any(self,pattern):
        match_object = re.search(pattern, self.__text)
        if match_object:
            print("Match found!")
        else:
            print("No match found!") 
            
    def replace(self,find,replace):
        result = re.sub(find,replace, self.__text)
        print (result)
 
            
    def find_all(self,pattern):
        matches = re.findall(pattern, self.__text)
        print (matches)
        
    def find_list(self,pattern):
        match_iterator = re.finditer(pattern, self.__text)
        for match_object in match_iterator:
            print(match_object.group(),"start=",match_object.start(),"end=",match_object.end())
            
    def compile(self,pattern):
        keyword = re.compile(pattern)
        exists = keyword.search(self.__text)
        if exists:
            print (f"pattern \"{pattern}\" exists",exists.group(0))
            
if __name__ == "__main__":
    pf = PatternFinder("I love Python. Python is easy to learn, and there are fun ways to learn Python ")
    pf.find_begin('Python')
    pf.find_any('Python')
    pf.find_all('Python')
    pf.find_list('Python')
    pf.replace(r'Python',r'Golang')
    pf.compile('Python')