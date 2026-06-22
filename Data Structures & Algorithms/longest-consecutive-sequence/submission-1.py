class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        num_set = set(nums)
        for i in range(len(nums)):
            if nums[i] - 1 not in num_set:
                current = nums[i]
                length = 1

                while current + 1 in num_set:
                    current += 1
                    length += 1
                longest = max(longest, length)
        return longest

        