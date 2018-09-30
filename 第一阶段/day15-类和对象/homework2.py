# @Author   :xaidc
# @Time     :2018/9/7 18:52
# @File     :homework2.py

'''
1.建立一个汽车类Auto，包括轮胎个数，汽车颜色，车身重量，速度等成员变量，并通过不同的构造方法创建实例。
至少要求 汽车能够加速 减速 停车。
再定义一个小汽车类CarAuto 继承Auto 并添加空调、CD等成员变量 覆盖加速 减速的方法
'''
class Auto:
    def __init__(self, tyre_num,color,weight,speed):
        self.tyre_num =tyre_num
        self.color = color
        self.weight = weight
        self.speed = speed
    def speed_up(self,accelerated_speed):
        self.speed += accelerated_speed
        print('正在加速')
        return '加速度为%d'%accelerated_speed
    @classmethod
    def speed_down(cls):
        return '正在减速'

    @staticmethod
    def park():
        return '已停车'
class CarAuto(Auto):
    def __init__(self,tyre_num,color,weight,speed):
        super().__init__(tyre_num,color,weight,speed)
        self.air_conditioner =  '格力'
        self.cd = 'cd12'



A1 = Auto(4,'黑色','2000kg',56)
print(A1.speed_up(5))
print(A1.speed_down())
print(A1.park())
print('===================')
C1 = CarAuto(4,'baise','1000kg',78)
print(C1.air_conditioner)
print(C1.cd)
print(C1.speed_up(6))
print(C1.speed_down())