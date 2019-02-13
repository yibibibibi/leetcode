class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def tosaystring(string):
            '''
            :type string : str 
            :rtype : str
            '''
            prechar = string[0]
            res = ''
            times = 0
            for char in string:
                if char == prechar:
                    times += 1 # 每一个字符出现的次数，初始为1，出现相同的加1
                else:
                    res += str(times)+str(prechar)  
                    times = 1  # 初始化次数
                    prechar = char 
            res += str(times)+str(prechar) # 添加最后一个数字和它的出现次数
            return res
        res = '1'  # 初始字符串为 "1"
        for i in range(n-1):   # 根据提示，若想知道报的第n次数，只需知道报的第n-1次是什么就可以。
            res = tosaystring(res)  
        return res
