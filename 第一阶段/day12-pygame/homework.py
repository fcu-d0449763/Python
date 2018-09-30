# @Author   :xaidc
# @Time     :2018/9/4 17:04
# @File     :homework.py
import pygame
from random import randint
pygame.init()
window = pygame.display.set_mode((600, 600))
window.fill((255, 255, 255))
pygame.display.flip()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            x,y = event.pos
            # pygame.draw.circle(window,(randint(0,255),randint(0,255),randint(0,255)),(x,y),50)
            # pygame.display.flip()

            r = randint(1,100)
            y_speed = 1
            x_speed = 2
            while True:
                # 将之前纸上的内容给覆盖
                window.fill((255, 255, 255))
                # 不断的画圆
                pygame.time.delay(5)
                # pygame.draw.circle(window, (255, 0, 0), (x, y), r)
                pygame.draw.circle(window, (255,255,0), (x, y), r)
                pygame.display.update()
                # 改变y值让圆在垂直方向移动
                y += y_speed
                x += x_speed
                if y > 600 - r:
                    y = 600 - r
                    y_speed *= -1
                elif y < 50:
                    y = 50
                    y_speed *= -1
                if x > 600 - r:
                    x = 600 - r
                    x_speed *= -1
                elif x < 50:
                    x = 50
                    x_speed *= -1
