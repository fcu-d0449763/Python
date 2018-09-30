# @Author   :xaidc
# @Time     :2018/9/12 11:08
# @File     :01-socket编程.py
'''
socket又叫套接字,就是进行数据通信两端.分为服务端套接字和客户端套接字
套接字编程:自己写服务端或者客户端,进行数据传输

python对socket编程的支持:提供了一个socket的库(内置)
'''
import socket
def creat_server():
    '''写一个服务器'''
#     1.创建套接字对象
    """
    socket(family,type)
    a.family:确定IP协议类型
    AF_INET:ipv4(默认)
    AF_INET6:ipv6
    b.type:传输协议类型
    SOCK_STREAM:TCP协议(默认)
    SOCK_DGRAM:UDP协议
    """
    server = socket.socket()
#     2.绑定IP地址和端口
#     bind((ip地址,端口))
#     端口:一台电脑上一个端口标记一个唯一的服务.范围0~65535,0~1024是著名端口,专门用来标记一些特殊的服务
#     但是,同一个端口同一时间只能绑定一个服务
    server.bind(("10.7.153.149",8081))
#     3.开始监听(监听客户端的请求)
    """
    listen(最大个数)
    同一时间能够连接的客户端的个数
    """
    server.listen(520)
    connect, address = server.accept()
    print(address)
#     4.让服务器处于运行状态
    while True:
        # print('监听状态')
        #5. 连接客户端(建立连接),返回连接对象
#         这句代码会阻塞线程,直到有客户端来请求当前服务器为止

#         6.服务器给客户端发送消息
        '''
        send(data)
        data:python3中要求类型是bytes,python2可以是字符串
        1.字符串(str)转二进制(bytes):
        字符串.encode(编码方式)-----编码方式默认值是 'utf-8'
        bytes(字符串,编码方式)
        '''
        message = input("服务器:")
        connect.send(message.encode())
        # connect.send(bytes('哈哈哈哈','utf-8'))

#         7.接受从客户端发送过来的消息
#         注意:recv方法也会阻塞线程
        '''
        recv(bufsize)
        bufsize:每次能够接受的最大的字节数
        返回值:接受到的数据,类型是bytes
        
        2.二进制转字符串:
        二进制.decode()
        str(二进制,编码方式)
        '''
        recv_data = connect.recv(1024)
        # print(recv_data.decode())
        print(str(recv_data,'utf-8'))
#       8.断开连接
    connect.close()

if __name__ == '__main__':
    creat_server()