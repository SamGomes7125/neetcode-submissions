class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = []
        result = []
        index = 0
        def backtrack(index):
            if index == len(nums):
                result.append(subset.copy())
            else:
                subset.append(nums[index])
                backtrack(index+1)
                subset.pop()
                backtrack(index+1)
        backtrack(index)
        return result


        