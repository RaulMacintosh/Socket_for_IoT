import socket
import time

potentiometer = "1023\n"
ldr = "30%\n"
other = ""

def client_thread(command):
    # Protocol: 
    #   * 'a' -> get potentiometer value
    #   * 'b' -> get LDR value
    #   * 'c' -> set on/off red LED
    #   * 'd' -> set on/off yellow LED
    #   * 'e' -> set on/off green LED

    HOST = '192.168.25.8'
    PORT = 5000
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    dest = (HOST, PORT)

    tcp.connect(dest)

    global potentiometer
    global ldr
    global other

    if command == "PT":
        tcp.send('a')
        time.sleep(1)
        potentiometer = tcp.recv(1024)
    elif command == "LR":
        tcp.send('b')
        time.sleep(1)
        ldr = tcp.recv(1024)
    elif command == "L1":
        tcp.send('c')
        time.sleep(1)
        other = "Red LED\n"
    elif command == "L2":
        tcp.send('d')
        time.sleep(1)
        other = "Yellow LED\n"
    elif command == "L3":
        tcp.send('e')
        time.sleep(1)
        other = "Green LED\n"
    else:
        other = "[ERROR] - Command not defined!\n"

    tcp.close()

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

            if command == "EX":
                print 'Finishing connection with ', cliente
                con.close()
                break
            else:
                client_thread(command)

                if command == "PT":
                    con.send(potentiometer)
                elif command == "LR":
                    con.send(ldr)
                else:
                    con.send(other)

server_thread()