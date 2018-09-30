# @Author   :xaidc
# @Time     :2018/9/4 10:57
# @File     :05-显示文字.py

import pygame
# 初始化游戏和创建窗口
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((255,255,255))
# 显示文字
# 1.创建字体对象
"""
a.创建系统的字体对象
SysFont(name, size, bold=False, italic=False, constructor=None)
name:字体名（系统支持的字体名）
size：字体大小
bold：是否加粗
italic：是否倾斜


b. 创建自定义的字体对象
Font(字体文件路径，字体大小)
字体文件路径：ttf文件
"""
# a.创建系统字体
# font = pygame.font.SysFont('Times',30)

# b.创建自定义字体
font = pygame.font.Font('./files/aa.ttf',30)

image = pygame.image.load('./files/dcat.jpg')

new_image1 = pygame.transform.rotozoom(image,0,0.5)
image_width,image_height = new_image1.get_size()
# 2.根据字体创建文字对象
"""
render(self, text, antialias, color,background=None)
text:需要显示的文字（字符串）
antialias：是否平滑（布尔）
color：颜色
background:
"""
text = font.render('你好，江秀成',True,(0,0,255),(0,200,100))

x,y = text.get_size()

# 3.渲染文件
window.blit(new_image1,(0,0))
window.blit(text,(x,image_height+10))

# 4.展示内容
pygame.display.flip()

# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()