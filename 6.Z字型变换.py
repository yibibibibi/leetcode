class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows <= 1:
            return s
        res = ''
        size = numRows*2 - 2
        length = len(s)
        
        for i in range(numRows):
            for j in range(i,length,size):
                res += s[j]
                temp = j + size - 2*i
                if (i != 0 and i != numRows-1 and temp<length):
                    res += s[temp]
        return res
