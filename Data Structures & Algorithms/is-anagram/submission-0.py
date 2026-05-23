class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = True
        dic1 = {}
        dic2 = {}
        if len(s) != len(t):
            c = False 
        else:
            for i in range(len(s)):
                if s[i] not in dic1:
                    dic1[s[i]] = 1
                else:
                    dic1[s[i]] += 1
            for i in range(len(t)):
                if t[i] not in dic2:
                    dic2[t[i]] = 1
                else:
                    dic2[t[i]] += 1
            if dic1 != dic2:
                c = False
        return c
                
            


