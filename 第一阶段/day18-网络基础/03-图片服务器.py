# @Author   :xaidc
# @Time     :2018/9/12 15:20
# @File     :03-图片服务器.py
import socket

if __name__ == '__main__':
    # 1.创建套接字(创建一个座机)
    server = socket.socket()
    # 2.绑定地址(插电话线,绑定电话号码)
    server.bind(('10.7.153.149',12345))
    # 3.监听(人坐在电话旁)
    server.listen(520)
    # 保证电话可以被打通(等)
    while True:
        # 4.接受请求(接电话)
        connect,adrr = server.accept()
        # 5.发送数据(讲电话)
        with open('./files/dcat1.jpg','br') as f:
            data = f.read()
        connect.send(data)

        # 6.接收数据(听)
        # connect.recv(1024)

        # 7.关闭连接(挂)
        connect.close()