import glob
  
files = glob.glob('./**/*.py', recursive = True)
for file in files:
    print(file)
print (len(files), "files found")