import socket

s = socket.socket()
port = 9001

s.connect(('127.0.0.1',port))

msg = s.recv(1024)

print('Server',"=>", msg.decode())


reply = 'Thanks for letting me in'
print ("Reply to Server","=>",reply)
s.send(reply.encode())    

s.close()