class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == '0' or num2 =='0': # 如果有一个数值为0就返回0
            return '0'
        l1 = len(num1); l2 = len(num2)
        k = l1+l2 -2
        res = [0]*(l1+l2)
        for i in range(l1):   # 返回每一位的未进位的值
            for j in range(l2):
                res[k-i-j]  += (int(num1[i]))*(int(num2[j]))
        carry = 0
        for i in range(len(res)):  # 循环进位显示每一位的值
            res[i] += carry
            carry = res[i]//10
            res[i] %= 10
        
        i = -1
        while res[i] == 0:  # 找到非0数位的索引
            i -= 1
       # 列表输出字符串
        return ''.join(map(str,res[::-1])) if i == -1 else ''.join(map(str,res[:i+1][::-1]))
