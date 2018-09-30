# @Author   :xaidc
# @Time     :2018/9/5 20:37
# @File     :game1.py

import pygame
pygame.init()
pygame.display.set_mode((600,600))
window = pygame.display.set_caption('games')
window.fill((255,255,255))
pygame.display.flip()




while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

