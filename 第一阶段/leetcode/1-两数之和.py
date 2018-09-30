# @Author   :xaidc
# @Time     :2018/8/31 19:50
# @File     :1-两数之和.py
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                x = nums[i] +nums[j]
                if target == x:
                    x1 = i
                    x2 = j
                    break
        list1= []
        list1.append(x1)
        list1.append(x2)
        return list1
    list2 = twoSum(0,[2,7,11,15],9)
    print(list2)