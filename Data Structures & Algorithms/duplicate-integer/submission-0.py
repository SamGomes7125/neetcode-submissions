class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_num = {}
        c = False
        for i in range(len(nums)):
            if nums[i] not in hash_num:
                hash_num[nums[i]] = True
            else:
                c = True
                break
        return c