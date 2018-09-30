# @Author   :xaidc
# @Time     :2018/9/12 18:41
# @File     :homework_client.py
import socket

def creat_client():
    client = socket.socket()
    client.connect(('10.7.153.149', 8080))
    num = 0
    while True:
        while True:
            data = client.recv(1024)
            x = data.decode(encoding='utf-8')
            print(x)

            message = input("客户端%d:"%num)
            client.send(message.encode())
            if x == '拜拜':
                num += 1
                break
    client.close()
creat_client()