import os
import subprocess
import sys



def call_os(cmd):
    print ("\ncall_os")
    returned_value = os.system(cmd)
    if not returned_value:
        print ("command executed successfully")

def call_subprocess(cmd):
    print ("\ncall_subprocess")
    returned_value = subprocess.call(cmd, shell=True)
    if not returned_value:
        print ("command executed successfully")

def process_output(cmd):
    print ("\nprocess_output")
    returned_value = subprocess.check_output(cmd)
    print (returned_value.decode('utf-8'))

if __name__ == "__main__":
    cmd = "git --version"
    call_os(cmd)

    call_subprocess(cmd)

    cmd = ["git","--version"]
    process_output(cmd)

    print ("CWD",os.getcwd() )
    try:
        os.mkdir(os.getcwd()+"/tmp")
    except FileExistsError:
        os.rmdir(os.getcwd()+"/tmp")
    except Exception as e:
        print ("some other error")
    else:
        print ("mkdir successful")
    finally:
        print ("mkdir operation completed")
    os.chdir('../') 
    print ("CWD",os.getcwd() )
    print (os.listdir(os.getcwd()) )

    print(sys.argv[0])
    print('Number of arguments present =', len(sys.argv))
    print('Total argument list:', str(sys.argv))
    print (sys.path)

    # python interpreter's version number.
    print (sys.version)

    input_words = []
    for words in sys.stdin: 
        if 'quit' == words.rstrip(): 
            break
        print(f'Input : {words}') 
        input_words.append(words)
  
    print("Exited! Entered list of words are", input_words)
    print ("OS Platform=",sys.platform)
    print ("Count of modules installed=",len(sys.modules))
    sys.exit(1)