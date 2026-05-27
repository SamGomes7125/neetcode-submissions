class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        h1 = {}
        for i in range(len(s1)):
            if s1[i] not in h1:
                h1[s1[i]] = 1
            else:
                h1[s1[i]] += 1
        h2 = {}
        
        for i in range(len(s2)-len(s1)+1):
            h2 = {}
            for j in range(len(s1)):
                if s2[i+j] not in h2:
                    h2[s2[i+j]] = 1
                else:
                    h2[s2[i+j]] += 1
            if h1 == h2:
                return True
        return False


        