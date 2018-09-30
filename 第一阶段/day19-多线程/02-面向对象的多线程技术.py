# @Author   :xaidc
# @Time     :2018/9/13 11:09
# @File     :02-面向对象的多线程技术.py
from threading import Thread
import datetime
import time
from random import randint
'''
面向对象实现多线程技术
1.声明一个类继承自Thread类
2.重写run方法,将需要在子线程中执行的任务放到run方法中
3.在需要子线程的位置去创建这个类的对象,然后用对象调用start方法去执行run中的任务
'''
#注意:继承的时候,可以继承自己写的类,也可以继承系统的类或者别人写好的类
class Download(Thread):
    """下载线程类"""
    def __init__(self,file):
        super().__init__()
        self.file = file
    def run(self):
        print(self.file+'开始下载:',datetime.datetime.now())
        time.sleep(randint(5,10))
        print(self.file+'下载结束:',datetime.datetime.now())

if __name__ == '__main__':
    print('===========')
    t1 = Download('沉默的羔羊')
    t1.start()
    t2 = Download('恐怖游轮')
    t2.start()
    print('+++++++++++')