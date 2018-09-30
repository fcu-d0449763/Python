# @Author   :xaidc
# @Time     :2018/9/4 15:25
# @File     :model.py
import pygame
pygame.init()
window = pygame.display.set_mode((400, 600))
window.fill((255, 255, 255))



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()