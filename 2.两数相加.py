# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0) # 头结点是一个0节点
        current = res
        y = 0
        while l1 or l2 or y:
            addnum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + y
           
            y = addnum/10   # y用于存储进位数
            current.next = ListNode(addnum%10) # current.next 链接每一位的值
            current = current.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return res.next
