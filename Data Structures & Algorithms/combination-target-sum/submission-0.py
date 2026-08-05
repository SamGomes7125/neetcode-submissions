class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combination = []
        combination_sum = []
        index = 0
        total = 0
        def dfs(index, total):
            if total == target:
                combination_sum.append(combination.copy())
                return
            if total > target:
                return
            if index == len(nums):
                return
            else:
                combination.append(nums[index])
                dfs(index,total+nums[index])
                combination.pop()
                dfs(index+1,total)
        dfs(index,total)
        return combination_sum


        
        