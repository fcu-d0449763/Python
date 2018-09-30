# @Author   :xaidc
# @Time     :2018/9/5 9:03
# @File     :01-ballgame.py
import pygame
import jxc_color
from random import randint
"""
游戏功能：点击屏幕再点击的地方产生一个小球，球可以自由的移动，撞到边界会弹回，撞到其他球会吃掉

第一步：搭建游戏窗口
第二步：点击屏幕产生球
第三步：让球动起来（需要用列表来保存所有的球，需要使用字典来保存每个球的信息）
第四步:大球吃小球
"""
# 全局变量
WINDOW_WIDTH = 600  #屏幕宽度
WINDOW_HIGHT = 400  #屏幕高度

key_ball_color = 'ball_color'
key_ball_center = 'ball_center'
key_ball_radius = 'ball_radius'
key_ball_xspeed = 'ball_xspeed'
key_ball_yspeed = 'ball_yspeed'
key_ball_alive = 'ball_alive'

all_balls = [] # 保存所有的球

def ball_crash():
    """
    检测碰撞
    :return:
    """
    #看屏幕上每个球是否和其他球的圆心距小于等于半径和
    #拿第一个球
    for ball in all_balls:
        # 拿另外一个球
        for other in all_balls:
            #是同一个球或者是已经消失的球都不需要再判断
            if ball == other or ball[key_ball_alive] == False or other[key_ball_alive] == False:
                continue
            # 判断两次拿到的球是否相撞
            x1,y1 = ball[key_ball_center]
            x2,y2 = other[key_ball_center]
            # 计算两个球的圆心距
            distance = ((x1 - x2)**2 +(y1 - y2)**2)**0.5
            if distance <= ball[key_ball_radius] + other[key_ball_radius]:
                # 相撞后：
                if randint(0,1):
                    ball[key_ball_radius] += int(other[key_ball_radius]*0.4)
                    other[key_ball_alive] = False  #一个球消失
                else:
                    other[key_ball_radius] += int(ball[key_ball_radius] * 0.4)
                    ball[key_ball_alive] = False  # 一个球消失


def draw_all_ball(window):
    """
    画所有的球
    :param window:
    :return:
    """
    window.fill(jxc_color.white)
    for ball in all_balls[:]:
        # 如果是活着的就画出来，如果已经死掉了就移除
        if ball[key_ball_alive]:
            pygame.draw.circle(window,ball[key_ball_color],ball[key_ball_center],ball[key_ball_radius])
        else:
            all_balls.remove(ball)
    pygame.display.update()


def ball_move():
    """
    球动起来
    :return:
    """
    for ball in all_balls:
        # 1.获取新的原点
        ball_x, ball_y = ball[key_ball_center]
        new_x = ball_x + ball[key_ball_xspeed]
        new_y = ball_y + ball[key_ball_yspeed]

        #2.做边界检测
        # x 方向的边界
        if new_x < ball[key_ball_radius]:
            new_x = ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1
        elif new_x > WINDOW_WIDTH - ball[key_ball_radius]:
            new_x = WINDOW_WIDTH - ball[key_ball_radius]
            ball[key_ball_xspeed] *= -1


        # y 方向的边界

        if new_y < ball[key_ball_radius]:
            new_y = ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1
        elif new_y > WINDOW_HIGHT - ball[key_ball_radius]:
            new_y = WINDOW_HIGHT - ball[key_ball_radius]
            ball[key_ball_yspeed] *= -1

        # 3.修改圆心坐标
        ball[key_ball_center] = new_x,new_y







def creat_ball(window,pos):
    """
    在指定的位置产生一个随机颜色的球
    :param window:
    :param pos:
    :return:
    """
    ball_color = jxc_color.rand_color()
    ball_center = pos
    ball_radius = randint(10,30)

    # 创建球对应的字典
    ball = {key_ball_color:ball_color,
            key_ball_center:ball_center,
            key_ball_radius:ball_radius,
            key_ball_xspeed:randint(-5,5),
            key_ball_yspeed:randint(-5,5),
            key_ball_alive:True
            }
    # 保存球的信息
    all_balls.append(ball)
    # 画球
    pygame.draw.circle(window,ball_color,ball_center,ball_radius)
    pygame.display.update()


def main_game():
    """
    游戏主系统
    :return:
    """
#     初始化游戏
    pygame.init()
    window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HIGHT ))
    pygame.display.set_caption('ballgame')
    window.fill(jxc_color.white)
    # 进入游戏界面默认显示的内容和要执行操作写到这儿。。。

    pygame.display.flip()


    # 游戏循环
    while True:
        pygame.time.delay(15)
        # 游戏循环执行的代码写在这儿。。。
        ball_move() # 修改球的位置
        ball_crash() # 检测球的碰撞
        draw_all_ball(window) #重新画所有的球

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            # 事件发生要执行的操作写到这个下面。。。
            elif event.type == pygame.MOUSEBUTTONDOWN:
                creat_ball(window,event.pos)
main_game()





