# @Author   :xaidc
# @Time     :2018/9/8 16:46
# @File     :hh.py
# 导入pygame和sys模块
import pygame, sys

# 初始化pygame、生成屏幕对象screen、显示标题字幕
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('hello world')

# 在屏幕(0, 0)的位置上绘制一个(50*50)大小的矩形
# 获取屏幕对象的矩形坐标
# 然后把矩形移动到屏幕指定的初始位置（屏幕正中央）
player = pygame.Rect(0, 0, 50, 50)
screen_rect = screen.get_rect()
player.centerx = screen_rect.centerx
player.centery = screen_rect.centery

# 设置上下左右移动标记，实现方块在按键以后持续移动
# 移动速度为 0.1 [否则移动太快无法看清楚方块的移动]
# 设置颜色值
moveLeft = False
moveRight = False
moveUp = False
moveDown = False
MOVESPEED = 0.1
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# 因为centerx和centery不能存储小数，所以要设置中间变量
player_x = float(player.centerx)
player_y = float(player.centery)

# 进入游戏大循环
while True:

    # 侦听事件，响应退出操作
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # 侦听事件，响应按键操作
        # 如果按下 <上下左右>键，则修改移动标记为True实现持续移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                moveLeft = True
            elif event.key == pygame.K_RIGHT:
                moveRight = True
            elif event.key == pygame.K_UP:
                moveUp = True
            elif event.key == pygame.K_DOWN:
                moveDown = True

        # 侦听事件，响应松键操作
        # 如果松开<上下左右>键，则修改移动标记为False停止移动
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                moveLeft = False
            elif event.key == pygame.K_RIGHT:
                moveRight = False
            elif event.key == pygame.K_UP:
                moveUp = False
            elif event.key == pygame.K_DOWN:
                moveDown = False

    # 如果移动标记为True并且方块player没有越过屏幕边界，那么持续移动
    # 将中间变量的值存储到centerx和centery中去
    # 从而改变方块的位置
    if moveDown and player.bottom < screen_rect.bottom:
        player_y += MOVESPEED
        player.centery = player_y
    if moveUp and player.top > screen_rect.top:
        player_y -= MOVESPEED
        player.centery = player_y
    if moveLeft and player.left > screen_rect.left:
        player_x -= MOVESPEED
        player.centerx = player_x
    if moveRight and player.right < screen_rect.right:
        player_x += MOVESPEED
        player.centerx = player_x

    # 每次循环都用白色填充屏幕
    # 么次循环重新绘制player方块
    # 每次循环都让元素在屏幕上可见
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, player)
    pygame.display.flip()
