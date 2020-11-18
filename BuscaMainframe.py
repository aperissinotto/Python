import socket

port = 23
msg = ''
erro = 0
uread = open('primeiro.ip', 'r')
uwrite = open('ultimo.ip', 'w')
radd = open('encontrado.ip', 'a')

host = uread.read()
print ('iniciando por: ' + host)

for ip1 in range(1, 255):
    for ip2 in range(1, 255):
        for ip3 in range(1, 255):
            for ip4 in range(1, 255):
                ipf = str(ip1) + '.' + str(ip2) + '.' + str(ip3) + '.' + str(ip4)
                a1 = (int(''.join(ipf.split('.'))))
                a2 = (int(''.join(host.split('.'))))
                if a1 < a2:
                    continue
                uwrite = open('ultimo.ip', 'w')
                uwrite.write(ipf)
                uwrite.close()
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
                    radd.write('n' + ipf)
                    print('find on ' + ipf)

print ('total de erros: ' + str(erro))

