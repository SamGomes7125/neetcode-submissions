class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        h = {}
        for num in nums:
            h[num] = num
        for i in range(len(nums)+1):
            if i not in h:
                return i
        return 0



        