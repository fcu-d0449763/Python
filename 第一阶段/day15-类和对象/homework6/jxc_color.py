# @Author   :xaidc
# @Time     :2018/9/5 9:19
# @File     :jxc-color.py

import random
# 白色
white = (255,255,255)
# 黑色
black = (0,0,0)
# 红色
red = (255,0,0)
# 绿色
green = (0,255,0)
# 蓝色
blue = (0,0,255)
# 灰色
gray = (120,120,120)
# darkgreen
dark_green = (0,155,0)

def rand_color():
    """
    随机颜色
    :return:
    """
    return random.randint(0,255),random.randint(0,255),random.randint(0,255)

if __name__ == '__main__':
    pass