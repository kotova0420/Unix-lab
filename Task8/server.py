import socket
import pickle
from random import randint

def encrypt(m, k):
    return ''.join([chr((ord(x) + k) % 65536) for x in m])

def decrypt(m, k):
    return ''.join([chr((ord(x) - k) % 65536) for x in m])

def free_port(p):
	try:
		sock = socket.socket()
		sock.bind(('',p))
		sock.close
		return p
	except:
		for _ in range(0, 65536):
			try:
				p=randint(0,65535)
				sock = socket.socket()
				sock.bind(('',p))
				sock.close
				return p
			except:
				continue    

HOST = '127.0.0.1'
port = 8080
sock = socket.socket()
port=free_port(port)          
sock.bind((HOST,port))
print('PORT:',port)

sock.listen(0)			
sock.setblocking(1)
conn, addr = sock.accept()
b = randint(1, 1000)
msg = conn.recv(1024)
(p, g, A) = pickle.loads(msg)

while True:
    msg = conn.recv(1024)
    if not msg:
        break
    
    msg = pickle.loads(msg)
    b = randint(1, 1000)
    B = g ** b % p
    k = A ** b % p
    print(k)
    conn.send(pickle.dumps((B, encrypt(msg, k))))

conn.close()