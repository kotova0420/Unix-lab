import socket
import pickle
from random import randint

def encrypt(m, k):
    return ''.join([chr((ord(x) + k) % 65536) for x in m])

def decrypt(m, k):
    return ''.join([chr((ord(x) - k) % 65536) for x in m])

HOST = 'localhost'

try:
    PORT=int(input("PORT:"))
    if not 0 <= PORT <= 65535:
        raise ValueError
except ValueError :
    PORT = int(input('Что-то пошло не так, попробуйте еще раз -->   '))

sock = socket.socket()
sock.connect((HOST, PORT))

p, g, a = randint(1, 1000), randint(1, 1000), randint(1, 1000)

A = g ** a % p

sock.send(pickle.dumps((p, g, A)))



while True:
    tt = input('Сообщение --> ')
    if tt == "":
        break
    
    sock.send(pickle.dumps(tt))
    msg = sock.recv(1024)
    B = pickle.loads(msg)[0]
    msg = pickle.loads(msg)[1]
    print(msg)
    k = B ** a % p
    print(decrypt(msg, k))

sock.close()