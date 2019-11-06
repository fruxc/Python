import socket

s = socket.socket()

print("Socket Successfully Created!!!")

port = 12345

s.bind(('', port))

print("Socket binded to %s"%(port))

s.listen(50)

print("Socket is listening")
con = 1
while con==1:
    c, addr = s.accept()
    print("Got connection from ", addr)
    c.send(b"Thank you for connecting ")
    c.close()
    con = con + 1
s.close()