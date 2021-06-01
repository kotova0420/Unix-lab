import asyncio

while True:
    file=open('Sokolova_file','a')
    HOST = input('Введите адрес хоста:\n')
    file.write("Запрашиваю адрес хоста\n")
    if HOST=='localhost':
        HOST='127.0.0.1'
        file.write(f"Введенный адрес хоста: {HOST} \n")
        file.close()
        break
    if HOST=='':
        file.write("Адрес хоста не установлен. \n")
        file.close()
        break
    host_l=HOST.split('.')
    if (0<=int(host_l[0])<255) and (0<=int(host_l[1])<255) and (0<=int(host_l[2])<255) and (0<=int(host_l[3])<255):
        file.write(f"Введенный адрес хоста: {HOST} \n")
        file.close()
        break
    else:
        print('Введен неверный формат адреса.')
        file.write("Введен неверный адрес хоста, запрашиваю адрес снова.\n")


while True:
    file=open('Sokolova_file','a')
    PORT=input('Введите номер порта от 1024 до 49151: \n')
    PORT=int(PORT)
    file.write("Запрашиваю номер порта...\n")
    if 1023<PORT<49152:
        file.write(f"Введенный номер порта: {PORT} \n")
        file.close()
        break
    else:
        print('Неверный номер порта.')
        file.write("Введен неверный номер порта, запрашиваю номер снова...\n")


async def handle_echo(reader, writer):
    data = await reader.read(100)
    writer.write(data)
    await writer.drain()

    writer.close()

loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle_echo, HOST, PORT, loop=loop)
server = loop.run_until_complete(coro)

# Обслуживайте запросы до тех пор, пока не будет нажата клавиша Ctrl+C
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Закрываем сервер
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()