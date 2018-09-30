# @Author   :xaidc
# @Time     :2018/9/4 11:29
# @File     :06-显示图形.py
import pygame
from math import pi
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((255,255,255))

"""
1.画直线
def line(Surface, color, start_pos, end_pos, width=1)
Surface:画在哪儿
color：线的颜色
start_pos:起点
end_pos:终点
width:线宽
"""
pygame.draw.line(window,(255,0,0),(50,100),(200,100))
pygame.draw.line(window,(255,0,0),(50,100),(50,200))

"""
2.画线段（折线）
def lines(Surface, color, closed, pointlist, width=1)
Surface:画在哪儿
color：颜色
closed：是否闭合
pointlist：点对应的列表
"""
pygame.draw.lines(window,(0,255,0),True,[(100,200),(230,245),(450,500)])

"""
3.画圆
def circle(Surface, color, pos, radius, width=0)
Surface：画在哪儿
color：颜色
pos：圆心坐标
radius：半径
width：线宽，0->填充
"""
pygame.draw.circle(window,(255,255,0),(300,300),100)
"""
4.画矩形
def rect(Surface, color, Rect, width=0)
Surface：画在哪儿
color：颜色
Rect：范围(元组，元组中有四个元素，分别是x,y,width,height)


"""
pygame.draw.rect(window,(200,100,200),(0,0,50,100))
"""
5.画多边形
def polygon(Surface, color, pointlist, width=0)
"""
# pygame.draw.polygon(window,(0,0,255),[(0,0),(100,500),(200,100),(400,300)])
"""
6.画椭圆
def ellipse(Surface, color, Rect, width=0)
"""
pygame.draw.ellipse(window,(0,255,255),(0,0,50,100))
"""
7.画弧线
def arc(Surface, color, Rect, start_angle, stop_angle, width=1)
"""
pygame.draw.arc(window,(200,120,10),(400,400,200,200),-(pi/2),(pi/2))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


