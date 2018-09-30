# @Author   :xaidc
# @Time     :2018/9/13 10:27
# @File     :01-多线程技术.py

'''
1.主线程:
每个进程默认都会有一个线程,这个线程我们一般都叫它主线程
默认情况下,所有的代码都是在主线程中执行.
2.子线程
一个进程中可以有多个线程.除了主线程以外,其他的线程需要手动的添加

3.threading是python中的一个内置模块,用来支持多线程
a.Thread类
Thread类的对象就是线程对象,需要线程的时候,就创建这个类或者这个类的子类对象
b.threading.currentThread()-->用来获取当前线程对象


'''
import  threading
import datetime
import time
# 下载两个电影
def download(file):
    print('开始下载:'+file,datetime.datetime.now())
    # 让线程阻塞5秒
    time.sleep(5)
    print(file+'下载结束:',datetime.datetime.now())
if __name__ == '__main__':
    print('主线程中的代码')
    print(threading.currentThread())
    #1.在主线程中下载两个电影:总共耗时20秒
    # download('多来a梦')
    # download('沉默的羔羊')
    # 2.在两个子线程中去下载两个电影:总共耗时10秒
    """
    Thread(target=)
    target:需要在子线程中调用的函数的函数名
    args:函数的实参
    返回值:创建好的线程对象
    """
    t1 = threading.Thread(target=download,args=('多来a梦',))
    # 开始执行t1对应的线程中的任务
    t1.start()
    t2 = threading.Thread(target=download, args=('多来a梦',))

    # 想要在子线程中执行任务,必须通过线程对象调用start方法才行 v
    t2.start()
    print('==============')