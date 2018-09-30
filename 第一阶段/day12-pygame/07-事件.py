# @Author   :xaidc
# @Time     :2018/9/4 14:34
# @File     :07-事件.py
import pygame
import random
# 游戏初始化
pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))



# 游戏循环
while True:
    # 所有的事件处理入口就是这个for 循环
    # for循环中代码只有游戏事件发生后才会执行
    """
    a.事件的type：
    QUIT:关闭按钮被点击事件
    
    鼠标事件：
    MOUSEBUTTONDOWN 鼠标按下
    MOUSEBUTTONUP 鼠标弹起
    MOUSEMOTION 鼠标移动
    键盘事件：
    KEYDOWN 键盘按下
    KEYUP 键盘弹起
    
    
    b.事件的pos ----鼠标事件发生的位置（坐标）
    
    c.事件的key ---键盘事件被按的键对应的编码值
    """
    for event in pygame.event.get():
        # 不同的事件发生后，对应type值不一样
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # 鼠标按下要做的事情就写在这儿
            print(event.pos)
            print("鼠标按下")
        # 鼠标按下画一个球

        elif event.type == pygame.MOUSEBUTTONUP:
            print("鼠标弹起")
        elif event.type == pygame.MOUSEMOTION:
            print("鼠标正在移动")
            pygame.draw.circle(window, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)),event.pos,50)
            pygame.display.flip()
        elif event.type == pygame.KEYDOWN:
            print("键盘按下",chr(event.key))
        elif event.type == pygame.KEYUP:
            print("键盘弹起")
