class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = nums[::-1]  # 翻转列表
        res = 0	# 该变量用来说明前res位已经可以跳跃成功了
        for i in range(1,len(nums)): #从索引1开始遍历判断是否可以跳跃成功，如果可以更新res的值。
            if nums[i] >= i -res:
                res = i
        return res == len(nums) -1
