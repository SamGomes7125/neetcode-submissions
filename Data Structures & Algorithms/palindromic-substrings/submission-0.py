class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        def expand(left, right):
            c = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                c += 1

            return c
        for i in range(len(s)):
            odd = expand(i, i)
            even = expand(i, i + 1)

            res += odd + even
        return res
        
        