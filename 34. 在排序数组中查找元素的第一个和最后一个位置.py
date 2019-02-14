class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        def left_bound(nums, target):
            begin = 0
            end = len(nums) - 1
            while begin <= end:
                mid = (begin + end)/2
                if nums[mid] == target:
                    if mid == 0 or nums[mid-1] < target:
                        return mid
                    end = mid - 1
                elif target > nums[mid]:
                    begin = mid + 1
                elif target < nums[mid]:
                    end = mid -1
            return -1
        def right_bound(nums, target):
            begin = 0
            end = len(nums) -1
            while begin <= end:
                mid = (begin + end)/2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid+1] > target:
                        return mid
                    begin = mid + 1
                elif target > nums[mid]:
                    begin = mid + 1
                elif target < nums[mid]:
                    end = mid - 1
            return -1
        pos = [-1,-1]
        if len(nums) < 1:
            return pos
        pos[0] = left_bound(nums, target)
        pos[1] = right_bound(nums,target)
        return pos
