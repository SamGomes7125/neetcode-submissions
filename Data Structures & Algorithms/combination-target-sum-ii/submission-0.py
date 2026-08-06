class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combination = []
        combination_sum = []
        index = 0
        total = 0
        candidates.sort()
        def dfs(index, total):
            if total == target:
                combination_sum.append(combination.copy())
                return
            if total > target:
                return
            if index == len(candidates):
                return
            else:
                combination.append(candidates[index])
                dfs(index+1,total+candidates[index])
                combination.pop()
                while index+1 <= len(candidates)-1 and candidates[index+1] == candidates[index]:
                    index = index+1
                dfs(index+1,total)
        dfs(index,total)
        return combination_sum
        