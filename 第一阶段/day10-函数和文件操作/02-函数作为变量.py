# @Author   :xaidc
# @Time     :2018/8/31 9:28
# @File     :02-函数作为变量.py

'''
在python中，函数就是一种特殊的类型，其实就是在声明类型是function的变量
变量能做的事，函数都可以做

1.
'''

if __name__ == '__main__':
    # 1.使用一个变量给另外一个变量赋值
    a = 10
    b = a

    # 声明一个函数func1（声明了一个函数func1，func1就是一个变量
    def func1():
        print('hello python')

    # c也是一个函数
    c =func1
    func1()
    c()

    # 2.函数作为列表的元素
    list1 = [a,'10',100]
    list2 = []
    list3 = []
    for x in range(10):
        def func2(y):
            print(x+y)
        list2.append(func2)
        list3.append(func2(x))
    print(list2)
    print(list3)
    # list2[0]就是一个函数
    func = list2[0]
    print(func(100))

    # 调用list2中下标是1对应的函数，并且传参为10
    x = 10
    list2[0](10)

    # 直接将函数作为列表的元素
    funcs = [func1]
    funcs[0]()
    #3.将函数作为字典的值
    operation = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y,:x*y}
    result = operation['+'](10,20)
    print(result)

    # 4.函数作为函数的参数（回调函数）
    def clean_kitchen(time):
        print("在%s，打扫厨房"%time)
        print("收费200元")
        return 200
    def clean_floor(time):
        print("在%s，做地板清洁服务")
        print("收费100元")
        return 100
    # 在指定的时间，叫指定的服务
    def call_service(time:str,service):
        service(time)
    call_service('上午十点',clean_kitchen)

    # 5.函数作为函数的返回值

    def operation(operator:str):
        if operator =='+':
            def my_sum(*nums):
                sum1 = 0
                for num in nums:
                    sum1 += num
                print(sum1)
            return my_sum
        elif operator =='*':
            def my_sum(*nums):
                sum1 = 1
                for num in nums:
                    sum1 *= num
                print(sum1)
            return my_sum
    operation('+')(1,2,3)
