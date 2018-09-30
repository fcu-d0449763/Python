# @Author   :xaidc
# @Time     :2018/9/4 10:33
# @File     :04-形变.py
import pygame
# 初始化和创建窗口
pygame.init()
window = pygame.display.set_mode((600,600))
window.fill((255,255,255)) #填充窗口颜色
# 图片相关
# 1.加载图片（选图）
image = pygame.image.load('./files/timg.jpg')


"""
形变：
a 缩放(指定大小)
transform.scale(缩放对象，目标大小):将指定的对象缩放到指定的大小，会返回缩放后的对象
"""
new_image = pygame.transform.scale(image,(100,100))



"""
b 缩放（指定缩放比例）
rotozoom(Surface, angle, scale)
Surface:旋转缩放对象
angle：旋转的角度(0-360)
scale：缩放比例
"""
new_image1 = pygame.transform.rotozoom(image,0,0.8)
"""
c.旋转
rotate(Surface,angle)
Surface:旋转缩放对象
angle：旋转的角度(0-360)
"""

# 2.渲染图片
window.blit(new_image1,(50,50))

# 3.展示内容
pygame.display.flip()





# 游戏循环
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
