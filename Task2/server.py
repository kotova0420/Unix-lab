import binascii
import errno
import hashlib
import json
import logging
import os
import socket
import threading


# def clients_add():
#     conn, addr = sock.accept()
#     print("Пользователь подключен!")
#     print(addr)
#     data = conn.recv(1024)
#     CONNECTION_LIST.append((conn, addr))
#     thread_client = threading.Thread(target=broadcast_usr, args=[data, conn])
#     thread_client.start()


def accept_client():
    while True:
        # accept
        cli_sock, cli_add = sock.accept()
        uname = cli_sock.recv(1024)
        CONNECTION_LIST.append((uname, cli_sock))
        print('%s is now connected' % uname)
        thread_client = threading.Thread(target=broadcast_usr, args=[uname, cli_sock])
        print("thread_client is worked")
        thread_client.start()


def broadcast_usr(uname, cli_sock):
    while True:
        try:
            data = cli_sock.recv(1024)
            print(data)
            if data:
                print("{0} spoke".format(uname))
                b_usr(cli_sock, uname, data)
        except Exception as x:
            print(x)
            break


def b_usr(cs_sock, sen_name, msg):
    for client in CONNECTION_LIST:
        if client[1] != cs_sock:
            client[1].send(sen_name)
            client[1].send(msg)


if __name__ == "__main__":
    sock = socket.socket()

    port = 9090
    while True:
        try:
            sock.bind(('', port))
            print("Сервер запущен на порту -", port)
            # logging.info(f"Сервер запущен на порту - {port}")
            break
        except socket.error as e:
            if e.errno == errno.EADDRINUSE:
                print("Порт уже занят!")
                port += 1
                # logging.warning(f"Порт уже занят, изменение на порт номер: {port}")
            else:
                print("Ошибка в подключении! ", e)
                # logging.error(f"Ошибка в подключении! {e}")

    sock.listen(1)
    print("Начало прослушивания порта!")
    # logging.info("Начало прослушивания порта!")

    CONNECTION_LIST = []

    thread = threading.Thread(target=accept_client())
    thread.start()

    # while True:
    #     msg = ''
    #     print("Пользователь подключен!")
    #     print(addr)
    #
    #     flag = False
