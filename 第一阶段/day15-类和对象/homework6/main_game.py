# @Author   :xaidc
# @Time     :2018/9/8 10:22
# @File     :main_game.py
import pygame
import jxc_color
import sys

# 全局变量
WINDOW_WIDTH = 600  #屏幕宽度
WINDOW_HEIGHT = 600  #屏幕高度



def main_game():
    X = 600//2
    Y = 600//2
    # 初始化
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    pygame.display.set_caption('games')
    window.fill(jxc_color.white)
    pygame.display.flip()



    while True:

        move_x,move_y = 0,0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP or event.key == pygame.K_w:
                    move_y = -10
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    move_x = 10
                elif event.key == pygame.K_LEFT or event.key ==pygame.K_a:
                    move_x = -10
                elif event.key == pygame.K_DOWN or event.key == pygame.K_s:
                    move_y = 10
            elif event.type == pygame.KEYUP:
                move_x = 0
                move_y = 0


        Y = move_y + Y
        X = move_x + X

        Y = (Y + 600) % 600
        X = (X + 600) % 600
        window.fill(jxc_color.white)
        pygame.draw.circle(window, jxc_color.gray, (X, Y), 50)
        pygame.display.update()

main_game()