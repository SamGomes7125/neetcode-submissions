class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        Hash1 = {}
        
        
        for i in range(len(strs)):
            Hash = {}
            for j in range(len(strs[i])):
                if strs[i][j] not in Hash:
                    Hash[strs[i][j]] = 1
                else:
                    Hash[strs[i][j]] += 1
            s = ''.join(sorted(strs[i]))
            if s not in Hash1:
                Hash1[s] = [strs[i]]
            else:
                Hash1[s].append(strs[i])
        return list(Hash1.values())
            

        