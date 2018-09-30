# @Author   :xaidc
# @Time     :2018/9/12 18:32
# @File     :homework_server.py
# 1. 客户端和服务器聊天，可以一直聊天，直到一方发送’拜拜’。然后就可以和下一个人一直聊
import socket

def creat_server():
    server = socket.socket()
    server.bind(("10.7.153.149",8080))
    server.listen(520)
    connect,address = server.accept()

    while True:
        while True:
            message = input("服务器:")
            connect.send(message.encode())

            recv_data = connect.recv(1024)
            print(str(recv_data, 'utf-8'))
            if message == '拜拜':
                break

    connect.close()
creat_server()