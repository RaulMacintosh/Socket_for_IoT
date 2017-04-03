import socket
import time

from threading import Thread

def client_thread():
	HOST = '192.168.0.117'
	PORT = 5000
	tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	dest = (HOST, PORT)

	tcp.connect(dest)

	msg = "Hello\n"
	tcp.send(msg)

	time.sleep(1)
	print tcp.recv(1024)

	tcp_to_thing.close()

def server_thread():
    HOST = ''
    PORT = 5001
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(1)
    while True:
        con, cliente = tcp.accept()
        print 'Concetado por', cliente
        while True:
            msg = con.recv(1024)
            if not msg: break
            print cliente, msg
            con.send("Hello")
        print 'Finalizando conexao do cliente', cliente
        con.close()

thread_1 = Thread(target=client_thread)
thread_2 = Thread(target=server_thread)

#thread_1.start()
thread_2.start()