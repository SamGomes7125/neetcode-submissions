class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        index = 0
        nums.sort()
        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
            else:
                subset.append(nums[index])
                backtrack(index+1)
                subset.pop()
                while index + 1 < len(nums) and nums[index + 1] == nums[index]:
                    index = index+1
                backtrack(index+1)
                
        backtrack(index)
        return result
        