# @Author   :xaidc
# @Time     :2018/9/4 19:02
# @File     :homework1.py
import pygame
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.flip()

# 球的圆心坐标
x = 100
y = 100
x1 = 200
y1 = 200
#游戏循环
r = 50
r1= 40
y_speed = 1
x_speed = 2
y1_speed = 2
x1_speed = 1
while True:
    # 将之前纸上的内容给覆盖
    window.fill((255,100,255))
    # 不断的画圆
    pygame.time.delay(10)
    pygame.draw.circle(window,(255,0,0),(x,y),r)
    pygame.draw.circle(window, (255, 255, 0), (x1, y1), r1)
    pygame.display.update()
    # 改变y值让圆在垂直方向移动
    y += y_speed
    x += x_speed
    if y > 600 - r:
        y = 600 - r
        y_speed *= -1
    elif y < 50:
        y = 50
        y_speed *=-1
    if x > 600 - r:
        x = 600 - r
        x_speed *= -1
    elif x < 50:
        x = 50
        x_speed *=-1

    y1 += y1_speed
    x1 += x1_speed
    if y1 > 600 - r1:
        y1 = 600 - r1
        y1_speed *= -1
    elif y1 < 50:
        y1 = 50
        y1_speed *= -1
    if x1 > 600 - r1:
        x1 = 600 - r1
        x1_speed *= -1
    elif x1 < 50:
        x1 = 50
        x1_speed *= -1



    # 事件检测
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
