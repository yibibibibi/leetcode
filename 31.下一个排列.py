class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        def reverse(nums,i,j): # 翻转列表
             while i < j:
                 nums[i], nums[j] = nums[j], nums[i]
                 i, j = i+1, j-1
        
        length  = len(nums) - 1
        i = length - 1
        j = length
        while i >= 0 and nums[i] >= nums[i+1]:# 从后往前寻找第一个不大于的数nums[i]
            i -= 1
        if i >=0:
            while nums[j] <= nums[i]:# 从后往前寻找第一个大于nums[i]的数nums[j]索引j
                j -= 1
        nums[i],nums[j] = nums[j],nums[i]#交换数字
        reverse(nums,i+1,length)#翻转数组
