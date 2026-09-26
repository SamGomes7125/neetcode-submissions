class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0
        res = 0
        def expand(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return left, right
        for i in range(len(s)):
            left1, right1 = expand(i, i)
            left2, right2 = expand(i, i + 1)

            len1 = right1 - left1 - 1
            len2 = right2 - left2 - 1

            if len1 > resLen:
                resLen = len1
                res = s[left1 + 1:right1]

            if len2 > resLen:
                resLen = len2
                res = s[left2 + 1:right2]
        return res

        
            




        