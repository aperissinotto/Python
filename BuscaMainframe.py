import socket

port = 23
msg = ''
erro = 0

for ip1 in range(1, 255):
    for ip2 in range(1, 255):
        for ip3 in range(1, 255):
            for ip4 in range(1, 255):
                ipf = str(ip1) + "." + str(ip2) + "." + str(ip3) + "." + str(ip4)
                dest = (ipf, port)
                try:
                    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    socket.setdefaulttimeout(10.0)
                    tcp.connect(dest)
                    msg = tcp.recv(3)
                except socket.gaierror:
                    erro = erro + 1
                except socket.error:
                    erro = erro + 1
                if msg == b'\xff\xfd(':
                    print('find on ' + host)

print ('total de erros: ' + str(erro))
