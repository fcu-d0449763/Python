# @Author   :xaidc
# @Time     :2018/9/4 9:05
# @File     :02-pygame基本操作.py
import pygame
# 1.初始化游戏模块
pygame.init()

# 2.创建游戏窗口
'''
set_mode(窗口大小)：创建一个窗口并且返回
窗口大小：是一个元组，并且元组中需要两个值分别表示宽度和高度(单位是像素)
'''
window = pygame.display.set_mode((600,600))

# 3.让游戏一直运行，直到点关闭按钮才结束
while True:
    # 获取游戏过程中产生的所有的事件
    for event in pygame.event.get():
        # type来判断事件的类型
        if event.type == pygame.QUIT:
            exit() #退出程序
