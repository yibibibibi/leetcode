class Solution(object):
    def dfs(self,low,length,s,res,vaild,path=[]):
        if low == length:
            res.append(' '.join(path))
            return
        for i in range(low,length):
            if vaild[low][i]:
                self.dfs(i+1,length,s,res,vaild,path+[s[low:i+1]])
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """           
        length = len(s)
        vaild = [[False]*length for _ in range(length)]
        dp = [False for _ in range(length+1)]
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1,length+1):
            for j in range(i+1):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    dp[i] = True
                    vaild[j][i-1] = True
        res = []
        if dp[-1]:
            self.dfs(0,length,s,res,vaild)
        return res
                
