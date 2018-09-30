# @Author   :xaidc
# @Time     :2018/9/4 9:29
# @File     :03-显示图片.py
import pygame
pygame.init()
window = pygame.display.set_mode((700,700))
# 给窗口填充颜色
'''
fill(颜色)
颜色：计算机三原色（红，绿，蓝）不同，每个对应的值的范围是0-255.
可以通过改变三原色的值，可以调配出不同的颜色
颜色值：是一个元组，元组中三个元素，分别代表红绿蓝（rgb）
（255,0,0）--->红色
（0,255,0）--->绿色
（0，0，255）-->蓝色
（0,0,0）--->黑色
（255,255,255)-->白色
'''
window.fill((255,255,255))
'''
显示图片
image.load(图片路径)：获取本地的一张图片，返回图片对象
'''
# a.获取图片，创建图片对象
image = pygame.image.load('./files/timg.jpg')
"""
getsize():获取大小，返回值是一个元组，有两个元素，分别是宽和高
"""
image_width,image_height = image.get_size()

# b.渲染图片(将图片画在纸上)
"""
blit(渲染对象，位置)
位置：坐标（x，y），值的类型是元组，元组有两个元素分别对应x坐标和y坐标
"""
window.blit(image,(700-image_width,700-image_height))
# c.展示内容(将纸贴在画框上)
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
