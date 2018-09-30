# @Author   :xaidc
# @Time     :2018/9/13 11:32
# @File     :03-join方法的使用.py
from threading import Thread
import time
from datetime import datetime
from random import randint
# 在两个子线程中下载两个电影,在主线程中去统计两个电影下载的时间
"""
如果希望某个线程结束后才执行某个操作,就用那个线程调用join方法
"""
class Download(Thread):
    def __init__(self,file):
        super().__init__()
        self.file = file

    def run(self):
        print(self.file+'开始下载:',datetime.now())
        time.sleep(randint(5,15))
        print(self.file+'下载结束',datetime.now())
if __name__ == '__main__':
    t1 = Download('美丽人生')
    t2 = Download('怦然心动')

    start = time.time()
    time1 = t1.start()
    time2 = t2.start()
    #系统t1和t2中的代码都结束后才执行下面的代码
    t1.join()  #这句代码后面的代码在t1对应的线程结束后才执行
    t2.join()
    end = time.time()
    print(end-start)

