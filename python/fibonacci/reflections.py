class MyClass:
   def __init__(self, name):
      self.name = name

obj = MyClass("John")

# Reflection: Getting and setting attributes dynamically
print(getattr(obj, "name")) 

setattr(obj, "name", "Jane")
print(getattr(obj, "name"))