import shutil
 
src = "/home/User/Documents/file.txt"
 
dest = "/home/User/Documents/file.txt"
 
try:
    shutil.copy(src, dest)
    print("copy successful.")
 
except shutil.SameFileError:
    print("Source and destination objects are same.")
 
except PermissionError:
    print("Permission denied.")
 
except:
    print("Error occurred while copying file.")