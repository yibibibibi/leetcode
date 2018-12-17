"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Node
        :rtype: int
        """
     
        if root == None:
            return 0
        else:  
            depthes = []
            for child in root.children:
                depthes.append(self.maxDepth(child))
            maxdepth = 0 if depthes == [] else max(depthes)
            return maxdepth+1 
        
