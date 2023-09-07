class FileWrapper:

  def __init__(self, file):
    self.fileObj = file

  def __iter__(self):
    print ("__next__ is called")
    return self.fileObj.__iter__()

  def __next__(self):
    print ("__next__ is called")
    return self.fileObj.__next__()

  def __getattr__(self, item):

    return getattr(self.__dict__['fileObj'], item)


  def __setattr__(self, key, value):
    if key == 'fileObj':
      self.__dict__[key] = value
    else:
      setattr(self.__dict__['fileObj'], key,value)


  def __delattr__(self, item):
    delattr(self.__dict__['fileObj'], item)


if __name__ == '__main__':
  file = FileWrapper(open('decorator.txt', 'w'))
  file.write('testing')
  file.writelines("""
first line
second line
third line
  """)
  file.close()
  print ("Now let us render the contents",end="\n")
  with open("decorator.txt") as new_file:
    print(new_file.read())


