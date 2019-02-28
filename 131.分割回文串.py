class Solution:
    def dfs(self, low, high, s , res,dp, temp = []):
        if low == high:
            res.append(temp)
            return 
        for i in range(low, high):
            if dp[low][i]:
                self.dfs(i+1,high,s,res,dp,temp+[s[low:i+1]])
                
    def partition(self, s: str) -> List[List[str]]:
        length = len(s)
        dp = [[0]*length for _ in range(length)]
        for i in range(length):
            for j in range(length-i):
                if s[j] == s[j+i] and(i<2 or dp[j+1][j+i-1]==1):
                    dp[j][j+i] =1
        res = []
        self.dfs(0,length,s,res,dp)
        return res
    
