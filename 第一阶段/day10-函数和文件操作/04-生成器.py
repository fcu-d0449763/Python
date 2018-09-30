# @Author   :xaidc
# @Time     :2018/8/31 14:17
# @File     :04-生成器.py
def func1():
    print('abc')
    for x in range(10):
        yield x
        print('aaa')
'''
a.有yield的函数，在调用函数的时候不再是获取返回值
而是产生一个生成器对象，生成器对象中保留的是函数体
b.当通过next获取生成器中的数据的时候，才会去执行函数体，执行到yield为止
并且将yield后面的结果作为生成的数据返回，同时记录结束的位置，下次再调用next的时候
从上次结束的位置接着往后执行
'''
gen = func1()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
# 1.yield关键字
'''
只要函数中有yield关键字，那么这个函数就会变成一个生成器
这儿的func1（）是一个生成器
'''
# 注意：函数中只要有yield ，不管yield会不会执行到，函数的调用结果都是生成器
def func3(x):
    print('abc')
    if x > 10:
        yield 100
    return 20

# 练习：写一个生成器，可以产生斐波那契数列(可以无限生成)
print("===========")
def feibo(n):
    a = 1
    b = 1
    i = 1
    # print(1)
    while i<=n:
        c = a + b
        yield a
        a = b
        b = c
        i += 1
gen2 = feibo(11)
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))
print(next(gen2))

# 生成器和生成式产生的对象就是迭代器
iter1 = iter([1,2,3,4,])
print(iter1)
print(next(iter1))
