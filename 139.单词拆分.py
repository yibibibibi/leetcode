class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        length = len(s)
        dp = [False for _ in range(length+1)]
        dp[0] = True
        wordDict = set(wordDict)
        for i in range(1,length+1):
            for j in range(i+1):
                word = s[j:i]
                if dp[j] and word in wordDict:
                    dp[i] = True
                    break
        return dp[length]
