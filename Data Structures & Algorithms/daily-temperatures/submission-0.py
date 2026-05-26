class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = []
        for i in range(len(temperatures)):
            result.append(0)
        for i in range(len(temperatures)-1,0,-1):
            t1 = temperatures[i]
            for j in range(i):
                if temperatures[j]<t1:
                    result[j] = i-j
        return result
            

        