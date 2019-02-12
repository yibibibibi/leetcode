# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums == []:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])
        else:
            maxnum = max(nums)
            maxindex = nums.index(maxnum)
            root = TreeNode(maxnum)
            root.left = self.constructMaximumBinaryTree(nums[0:maxindex])
            root.right = self.constructMaximumBinaryTree(nums[maxindex+1:])
            return root
            
