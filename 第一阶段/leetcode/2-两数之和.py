# @Author   :xaidc
# @Time     :2018/9/15 15:14
# @File     :2-两数之和.py
'''

给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。

示例:

给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
'''
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num1 = 0
        num2 = 0
        list1 = [num1,num2]
        for i in range(len(nums)):
            if target >=0:
                if nums[i] <= target:
                    for j in range(i+1,len(nums)):
                        if nums[i] + nums[j] == target:
                            num1 = i
                            num2 = j
                            list1 = [num1,num2]
                            break
            if target < 0:


        return list1
c1 = Solution()
print(c1.twoSum([0,4,3,0],0))

