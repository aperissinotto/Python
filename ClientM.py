import socket
import ebcdic

HOST = "127.0.0.1"
PORT = 3280
CS = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print('Waiting for connection')
try:
    CS.connect((HOST, PORT))
except socket.error as e:
    print(str(e))
    exit(0)

print('Connected!!!')
while True:
    buffersend = input('Parla quelo que vuole: ')
    try:
        if buffersend == 'end':
            CS.close()
            exit(0)
        CS.sendall(buffersend.encode('cp1140'))
    except socket.error as e:
        print(str(e))
        CS.close()
        exit(0)
    
    print('Sended ok!!!')

    try:
        data = CS.recv(1024)
    except socket.error as e:
        print(str(e))
        CS.close()
        exit(0)

    print(data.decode('utf-8').encode('cp1140'))
