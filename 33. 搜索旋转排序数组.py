class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        def binsearch(nums, low, high, target):
            while low <= high:
                mid = (low+high)//2
                if nums[mid] == target:
                    return mid
                if nums[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            return -1
        def search2(nums, low, high, target):
            if (high < low): return -1
            mid = (low + high) // 2
            if nums[mid] == target: return mid
            if nums[low] <= nums[mid]:
                if nums[low] <= target and target < nums[mid]:
                    return binsearch(nums, low, mid-1, target)
                else:
                    return search2(nums, mid+1, high, target)
            else:
                if target > nums[mid] and target <= nums[high]:
                    return binsearch(nums, mid+1, high, target)
                else:
                    return search2(nums, low, mid-1, target)
        return search2(nums, 0, len(nums)-1, target)
