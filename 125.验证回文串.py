class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        rev = ''.join(filter(str.isalnum,s.lower()))
        return rev == rev[::-1]
