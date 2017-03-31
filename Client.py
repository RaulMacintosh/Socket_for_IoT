import socket
import time

HOST = '192.168.0.117'
PORT = 5000
tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dest = (HOST, PORT)

tcp.connect(dest)

msg = "Hello\n"
tcp.send(msg)

time.sleep(1)
print tcp.recv(1024)

tcp.close()