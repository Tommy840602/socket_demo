import socket

HOST = '127.0.0.1'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

outdata = input("enter:")

print('send: ',outdata)
s.send(outdata.encode())

indata = s.recv(1024)
print('recv: ' + indata.decode())

s.close()
