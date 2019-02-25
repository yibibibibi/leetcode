# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.res = 0          # 初始化一个res属性用来储存结果
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:    # 如果跟为空返回0
            return 0
        if root.right:# 如果有左子树，跟的值乘10加到左子树的val上
            root.right.val += 10 * root.val
        if root.left:# 有右子树，和上述操作一样
            root.left.val += 10 * root.val
        if not root.right and not root.left:# 如果是叶子节点res加上这个叶子结点的val
            self.res += root.val
        self.sumNumbers(root.right)# 递归处理左子树和右子树
        self.sumNumbers(root.left)
        return self.res
