import socket

s = socket.socket()
port = 9001
s.bind(("",port)) # empty string makes server listen to incoming requests, remember the tuple**
s.listen(5)
print ("\nsocket is listening\n")

while True:
    c,addr = s.accept()
    msg = b"Welcome, Buddy"
    print ("Server","=>",msg.decode())
    c.send(msg)

    reply = c.recv(1024)
    reply = reply.decode()
    print(addr[0],":",addr[1],"=>", reply,"\n")

    c.close()




