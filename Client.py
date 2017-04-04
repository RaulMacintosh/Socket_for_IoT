import socket
import time

temperature = "25 C\n"
humidity = "30%\n"
last_auth = "RFID Tag\n"
other = "[ERROR] - Command not defined!\n"

def client_thread(command):
    # Protocol: 
    #   * 'a' -> get temperature
    #   * 'b' -> get humidity
    #   * 'c' -> get last authentication
    #   * 'd' -> set on/off red LED
    #   * 'e' -> set on/off yellow LED
    #   * 'f' -> set on/off blue LED

    HOST = '192.168.0.117'
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)

    tcp.connect(dest)

    if command == "TMP":
        tcp.send('a')
        time.sleep(1)
        temperature = tcp.recv(1024)
    elif command == "HMD":
        tcp.send('b')
        time.sleep(1)
        humidity = tcp.recv(1024)
    elif command == "AUTH":
        tcp.send('c')
        time.sleep(1)
        last_auth = tcp.recv(1024)
    elif command == "LED 1":
        tcp.send('d')
        time.sleep(1)
        other = "LED 1"
    elif command == "LED 2":
        tcp.send('e')
        time.sleep(1)
        other = "LED 2"
    elif command == "LED 3":
        tcp.send('f')
        time.sleep(1)
        other = "LED 3"
    else:
        other = "[ERROR] - Command not defined!"

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
        print 'Connected with ', cliente

        while True:
            command = con.recv(2)
            con.recv(1024)

            if not command: break
            print cliente, command
            #client_thread(command)
            if command == "TP":
                con.send(temperature)
            elif command == "HM":
                con.send(humidity)
            elif command == "AU":
                con.send(last_auth)
            else:
                con.send(other)

        print 'Finishing connection with ', cliente
        con.close()

server_thread()