class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        l = len(nums)
        for i in range(l):
            d = target - nums[i]
            if d not in hash:
                hash[nums[i]] = i
            else:
                return sorted([hash[d], i])