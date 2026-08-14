class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        h = {}
        for i in range(len(nums)):
            if nums[i] in h:
                h[nums[i]]+=1
            else:
                h[nums[i]]=1
        for i in range(len(nums)):
            if h[nums[i]] == 1:
                return nums[i]
        