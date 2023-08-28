class FileWrapper:

  def __init__(self, file1):
    self.file2 = file1
    print (self.__dict__)

  def __iter__(self):
    print ("__next__ is called")
    return self.file2.__iter__()

  def __next__(self):
    print ("__next__ is called")
    return self.file2.__next__()

  def __getattr__(self, item):
    return getattr(self.__dict__['file2'], item)

  def __setattr__(self, key, value):
    if key == 'file2':
      self.__dict__[key] = value
    else:
      setattr(self.__dict__['file2'], key,value)

  def __delattr__(self, item):
    delattr(self.__dict__['file2'], item)


if __name__ == '__main__':
  test = open('decorator.txt', 'w')
  file = FileWrapper(open('decorator.txt', 'w'))
  #print (file1.__dict__)

  file.write('testing')
  file.writelines("""
first line
second line
  """)
  file.close()
  print (file.__dict__["file2"].__dict__)
  setattr(file,"page", 32)
  print (file.__dict__["file2"].__dict__)

