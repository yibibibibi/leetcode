# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        outlist = []
        if root == None:
            return outlist
        quene = [root]
        while quene:
            res = []
            i = 0
            queneNumber = len(quene)
            while i< queneNumber:
                point = quene.pop(0)
                res.append(point.val)
                if point.left:
                    quene.append(point.left)
                if point.right:
                    quene.append(point.right)
                i+=1
            outlist.append(res)
        return outlist
