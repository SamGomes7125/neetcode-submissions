class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = 0
        l = 0
        h = set()
        n = 0
        while r < len(s):
            
            while s[r] in h:
                h.remove(s[l])
                l += 1

            if s[r] not in h:
                h.add(s[r])
                
            
            if r-l+1 > n:
                n = r-l+1
            r += 1
        return n




        