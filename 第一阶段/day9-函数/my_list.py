# @Author   :xaidc
# @Time     :2018/8/30 15:32
# @File     :my_list.py

empty = []

def count(list1,item):
    """
    统计指定列表中指定元素的个数
    :param list1:
    :param item:
    :return:
    """
    num = 0
    for x in list1:
        if x ==item:
            num +=1
    return num