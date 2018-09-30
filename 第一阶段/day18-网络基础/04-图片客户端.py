# @Author   :xaidc
# @Time     :2018/9/12 15:31
# @File     :04-图片客户端.py
import socket

if __name__ == '__main__':
    client = socket.socket()
    client.connect(('10.7.153.149',12345))
    # 创建一个空的二进制数据
    all_data = bytes()
    # 接受从服务器传回来的数据
    data = client.recv(1024)
    while data:
        print('接受到数据')
        # 拼接二进制数据
        all_data += data
        data = client.recv(1024)
    with open('./files/new.jpg','wb') as f:
        f.write(all_data)
    client.close()