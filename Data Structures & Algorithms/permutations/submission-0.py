class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        perm = []
        visited = set()
        result = []
        index = 0
        def backtrack():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return
            for num in nums:
                if num not in visited:
                    visited.add(num)
                    perm.append(num)
                    backtrack()
                    visited.remove(num)
                    perm.pop()
                else:
                    continue

        backtrack()
        return result
        