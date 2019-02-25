###方法一：滑动窗口
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i,j,ans = 0,0,0  #初始化滑动窗口，和子串的长度。
        charset = set()
        while i<n and j <n:
            if s[j] not in charset:  #如果s[j]不在集合中，集合就添加s[j],然后j自增1
          
                charset.add(s[j])
                j += 1
                ans = max(ans,j-i)  # 如果集合中大于最长无重复子串的长度，就更新ans
            else:               
                charset.remove(s[i]) #如果s[j]在集合中，滑动窗口的左边界向右移动一位。所以set就应该移除这一个s[i]。继续滑动右边界。
                i += 1
        return ans

'''
### 方法二:优化的滑动窗口
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        i,ans = 0,0
        charmap = {}
        for j in range(n):
            if s[j] in charmap:
                i = max(charmap[s[j]],i)  # 如果s[j]在set中，i = j' + 1
            ans = max(ans,j-i+1)
            charmap[s[j]] = j+1
        return ans
