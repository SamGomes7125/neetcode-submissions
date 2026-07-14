class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h = {}
        r = 0
        l = 0
        a = 0
        while r < len(s):
            if s[r] not in h:
                h[s[r]] = 1
            else:
                h[s[r]] += 1
            max_freq = max(h.values())
            window_length = r - l + 1
            if window_length - max_freq > k:
                h[s[l]] -= 1
                l += 1
            a = max(a,r-l+1)
            r+=1
            
        return a
            
                

            
        
        

        