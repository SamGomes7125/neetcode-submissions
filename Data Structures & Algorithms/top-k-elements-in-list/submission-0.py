class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Hash = {}
        Result=[]
        for i in range(len(nums)):
            if nums[i] not in Hash:
                Hash[nums[i]] = 1
            else:
                Hash[nums[i]] += 1
        sorted_items = sorted(Hash.items(), key=lambda x: x[1], reverse=True)

        for num, freq in sorted_items[:k]:
            Result.append(num)
        return Result