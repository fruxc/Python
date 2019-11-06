import socket

s = socket.socket()

host = '127.0.0.1'
port = 12345

s.connect((host, port))
s.send(b"Hello server!!!")

with open('recieved_file.txt','wb') as f:
    print("File opened")
    while True:
        print("Recieving data...")
        data = s.recv(1024)
        print("data = %s", (data))
        if not data:
            break
f.close()
print("File closed")
s.close()
print("Connection closed")

