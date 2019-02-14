# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def countFloor(root):  # 返回树的深度
            if not root:
                return 0
            else:
                return 1+ max(countFloor(root.left), countFloor(root.right))
        if not root:
            return True
        if (abs(countFloor(root.left) - countFloor(root.right))>1):
            return False
        else:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
            
