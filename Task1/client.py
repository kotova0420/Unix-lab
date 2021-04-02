import socket
from time import sleep

sock = socket.socket()
print("Начинаем соединение с сервером) ")
address = input("Вводим адрес для подключения --> ")
if not address or address == '':
    address = "localhost"

port = input("Вводим номер порта --> ")
if not port or port == '':
    port = 9090
sock.connect(('localhost', 9090))

connection = True

while True:

    print("Прием данных от сервера")
    data = sock.recv(1024)
    print(data.decode())

# sock.close()
    send = input()
    msg = send
    print("Началась отправка данных серверу!")
    sock.send(msg.encode())

    if data.decode() == "exit":
        sock.close()
        break

