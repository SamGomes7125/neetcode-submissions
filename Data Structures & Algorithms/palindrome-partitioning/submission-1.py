class Solution:
    def partition(self, s: str) -> List[List[str]]:
        partition = []
        result = []
        index = 0
        def recursion(index):
            if index == len(s):
                result.append(partition.copy())
                return
            else:
                for i in range(index, len(s)):
                    if s[index:i+1] == s[index:i+1][::-1]:
                        partition.append(s[index:i+1])
                        recursion(i + 1)
                        partition.pop()    
        recursion(0)
        return result
        